import calendar


week = {
    calendar.MONDAY: "MONDAY",
    calendar.TUESDAY: "TUESDAY",
    calendar.WEDNESDAY: "WEDNESDAY",
    calendar.THURSDAY: "THURSDAY",
    calendar.FRIDAY: "FRIDAY",
    calendar.SATURDAY: "SATURDAY",
    calendar.SUNDAY: "SUNDAY"
}


mm, dd, yy = map(int, input().strip().split())


print(
    week[
        calendar.weekday(yy, mm, dd)
    ]
)
