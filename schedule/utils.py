from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
    DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    MONTHS = ["NONE", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
              "Ноябрь", "Декабрь"]

    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.meetups = []
        self.user = user
        super(Calendar, self).__init__()

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s">%s</th>' % (
            self.cssclasses_weekday_head[day], self.DAYS[day])

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = '%s %s' % (self.MONTHS[themonth], theyear)
        else:
            s = '%s' % self.MONTHS[themonth]
        return '<tr><th colspan="7" class="%s">%s</th></tr>' % (
            self.cssclass_month_head, s)

    # formats a day as a td
    def formatday(self, day):
        meetups = self.meetups[day]
        data = ""
        for meetup in meetups:
            data += f"<li> {meetup} </li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {data} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek):
        week = ""
        for data, weekday in theweek:
            week += self.formatday(data)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    def formatmonth(self, query, withyear=True, **kwargs):
        meetups = self.user.meetups.get_meetups_from_context(query).filter(date__year=self.year, date__month=self.month).all()
        
        self.meetups = [[] for i in range(32)]
        for meetup in meetups:
            self.meetups[meetup.date.day].append(meetup.get_html_url)
        calendar = (
            '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        )
        calendar += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )
        calendar += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f"{self.formatweek(week)}\n"
        calendar += '</table>'
        return calendar
