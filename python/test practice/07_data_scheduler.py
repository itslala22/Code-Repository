"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""


from datetime import datetime

def date_passed(todays_date, scheduled_date):
    today_date_dt = datetime.strptime(f"{todays_date} {2024}", '%dth %B %Y')
    scheduled_date_dt = datetime.strptime(f"{scheduled_date} {2024}", '%dth %B %Y')

    if today_date_dt == scheduled_date_dt:
        print ("Scheduled date is today")
    if today_date_dt < scheduled_date_dt:
        print ("Scheduled date is yet to pass")
    else:
        print ("Scheduled date has passed")


date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
