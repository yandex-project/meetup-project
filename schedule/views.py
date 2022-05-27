import datetime
import calendar
from django.views.generic import ListView
from meetups.models import Meetup

from schedule.utils import Calendar


class ScheduleView(ListView):
    model = Meetup
    template_name = 'schedule/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar or get it from the url
        # returns error message if date does not exist
        try:
            date = get_date(self.request.GET.get('month', None))
        except Exception:
            context['date_error'] = '<h1>Такай даты не существует 🥶</h1>'
            return context

        self.request.GET._mutable = True
        self.request.GET.pop('month', None)
        query = self.request.GET

        # Instantiate our calendar class with today's year and date
        cal = Calendar(date.year, date.month, user=self.request.user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(query, withyear=True)
        context['calendar'] = html_cal
        context['prev_month'] = prev_month(date, query)
        context['next_month'] = next_month(date, query)

        return context


def get_date(cur_month):
    if not cur_month:
        return datetime.datetime.today()

    if cur_month.count('-') == 2:
        return datetime.datetime.strptime(cur_month, '%Y-%m-%d')
    else:
        return datetime.datetime.strptime(cur_month, '%Y-%m')


def prev_month(date, query):
    first = date.replace(day=1)
    month = first - datetime.timedelta(days=1)
    data = f'month={month.year}-{month.month}&{query.urlencode()}'
    return data


def next_month(date, query):
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    last = date.replace(day=days_in_month)
    month = last + datetime.timedelta(days=1)
    data = f'month={month.year}-{month.month}&{query.urlencode()}'
    return data
