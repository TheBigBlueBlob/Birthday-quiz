"""
birthday.py
Author: Liam S
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
name = str(input("Hello, what is your name? "))
month = str(input("Hi, " + name + " what was the name of the month you were born in? "))
year = int(input("And what year were you born in, " + name + " ? "))
day = int(input("And the day? "))
if month == "January":
    month = 1
if month == "February":
    month = 2
if month == "March":
    month = 3
if month == "April":
    month = 4
if month == "May":
    month = 5
if month == "June":
    month = 6
if month == "July":
    month = 7
if month == "August":
    month = 8
if month == "September":
    month = 9
if month == "October":
    month = 10
if month == "November":
    month = 11
if month == "December":
    month = 12
if month == todaymonth and day == todaydate:
    print("Happy birthday!")
if month == 10 and day == 31
    print("You were born on Halloween! ")
if month == 1 or month == 2 or month == 2:
    season = 1
if month == 4 or month == 5 or month == 6:
    season = 2
if month == 7 or month == 8 or month == 9:
    season = 3
if month == 10 or month == 11 or month == 12:
    season = 4
if year < 1980:
    gen = 1
if year == 1980
