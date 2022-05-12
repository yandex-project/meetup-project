from calendar import HTMLCalendar
from meetups.models import Meetup


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    def formatday(self, day, meetups):
        meetups_per_day = meetups.filter(date__day=day)
        data = ""
        for event in meetups_per_day:
            data += f"<li> {event.get_html_url} </li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {data} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, meetup):
        week = ""
        for data, weekday in theweek:
            week += self.formatday(data, meetup)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    def formatmonth(self, withyear=True):
        meetups = Meetup.objects.filter(
            date__year=self.year, date__month=self.month
        )
        calendar = (
            '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        ) 
        calendar += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )
        calendar += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f"{self.formatweek(week, meetups)}\n"
        return calendar
