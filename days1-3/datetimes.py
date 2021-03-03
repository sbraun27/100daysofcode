import sys
from datetime import date
from datetime import datetime
from datetime import timedelta

import winsound
duration = 1000
freq = 440

# datetime is a python module that deals with dates and times


def learning_datetime_and_date():
    today = datetime.today()
    print(f"Today is {today}.")
    # today is a datetime.datetime object

    today_date = date.today()
    print(f"Using date, today is {today_date}.")
    # type of today_date is a datetime.date object, which just has the date string

    this_month = today_date.month
    this_day = today_date.day
    this_year = today_date.year

    christmas = date(2021, 12, 25)
    days_til_xmas = (christmas - today_date).days

    if christmas is not today_date:
        print(f"Sorry, there are still {days_til_xmas} days until Christmas")
    else:
        print("Yay it's Christmas!!")


def datetime_timedelta_usage():
    t = timedelta(days=4, hours=10)
    # t is a datetime.timedelta object

    days_in_t = t.days
    # Just the ten hours since seconds can only go up to a maximum of 1 day. like a timewatch
    seconds_in_t = t.seconds
    # No such thing as timedelta.hours
    hours_in_t = t.seconds / 60 / 60

    eta = timedelta(hours=6)
    today = datetime.today()
    print(f"I will wake up at {today + eta}.")


def pomodoro_timer(work=25, short_break=5, long_break=15):
    work_periods = 0
    print("Time to work!\n")

    while work_periods < 4:
        end_work = datetime.now() + timedelta(minutes=work)
        while datetime.now() < end_work:
            print((end_work - datetime.now()), end="\r")

        winsound.Beep(freq, duration)

        if work_periods < 3:
            print(f"Take a short {short_break} minute break.")
            end_short_break = datetime.now() + timedelta(minutes=short_break)

            while datetime.now() < end_short_break:
                print((end_short_break - datetime.now()), end="\r")

        else:
            print(f"take a longer {long_break} minute break.")
            end_long_break = datetime.now() + timedelta(minutes=long_break)

            while datetime.now() < end_long_break:
                print((end_long_break - datetime.now()), end="\r")

        winsound.Beep(freq, duration)

        print("Alright, back to work!\n")
        work_periods += 1


if __name__ == "__main__":
    n = len(sys.argv)

    if n > 1 and n < 5:
        work = int(sys.argv[1])
        short_break = int(sys.argv[2])
        long_break = int(sys.argv[3])
    elif n < 2:
        work = 25
        short_break = 5
        long_break = 15
    else:
        print("Usage: python datetimes.py <work> <short_break> <long_break>")
        sys.exit(1)

    while True:
        pomodoro_timer(work, short_break, long_break)
