"""
birthday.py
Author: Liam S
Credit: Vincent
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
year = int(input("And what year were you born in, " + name + "?"))
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
if month == 10 and day == 31:
    print("You were born on Halloween! ")
if month == 12 or month == 1 or month == 2:
    season = "winter"
if month == 3 or month == 4 or month == 5:
    season = "spring"
if month == 6 or month == 7 or month == 8:
    season = "summer"
if month == 9 or month == 10 or month == 11:
    season = "fall"
if year < 1980:
    gen = "Stone Age"
if year >= 1980 and year < 1990:
    gen = "eighties"
if year >= 1990 and year < 2000:
    gen = "nineties"
if year >= 2000:
    gen = "two thousands"
print(name + ", you are a " +season+ " baby of the " + gen + ".")
