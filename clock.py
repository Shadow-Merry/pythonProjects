import time
import datetime
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
try:
    clear()
    new = datetime.date.today()
    date = datetime.datetime.strptime(input("Enter the Date: "), '%Y-%m-%d')
    inputDate = date.date()
    if inputDate.year < new.year:
        print(f"Enter the Year Correctly You Enter {inputDate.year}")
        year = 0
    elif inputDate.year == new.year:
        year = 0
    else:
        year = (inputDate.year - new.year) * 12
    if inputDate.month < new.month:
        month = new.month - inputDate.month
        month = year - month
    elif inputDate.month == new.month:
        month = year
    else:
        month = inputDate.month - new.month
        month = year + month
    if inputDate.day < new.day:
        date = 30 - new.day + inputDate.day 
    elif inputDate.day == new.day:
        date = 0
    else:
        date = inputDate.day - new.day
    print(f"End Date: {inputDate}")
    print(f"Started Date: {new}")
    print(f"You Have {month} Month And {date} Day")
    time.sleep(5)

except ValueError:
    print("Please Enter The Date in This Formate YEAR-MONTH-DAY")