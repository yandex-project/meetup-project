import datetime
import calendar
from django.views import generic
from meetups.models import Meetup

from schedule.utils import Calendar


class ScheduleView(generic.ListView):
    model = Meetup
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar or get it from the url
        date = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(date.year, date.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = str(html_cal) + '</table>'

        context['prev_month'] = prev_month(date)
        context['next_month'] = next_month(date)

        return context


def get_date(cur_month):
    if cur_month:
        year, month = (int(x) for x in cur_month.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()


def prev_month(date):
    first = date.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(date):
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    last = date.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
