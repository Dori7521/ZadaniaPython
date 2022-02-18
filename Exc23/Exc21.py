#Moduły

#1
import calendar
import numbers
from unittest import result

year = calendar.calendar(2020)
print(year)

#2
month =calendar.month(2020,6)
print(month)

#3
# import datetime

# date1 = datetime.datetime(2020,6,1)
# date2 = datetime.datetime(2020,7,18)
# difference = date2-date1
# print(difference)

from datetime import date
 
 
date1 = date(2020, 6, 1)
date2 = date(2020, 7, 18)
diff = date2 - date1
print(diff)

#4
import re

string = 'Python 3.8'
# result = re.findall(pattern=r"\d", string=string)
# print(result)
res = re.findall('\d',string)
print(res)

#5
string = '!@#$%^&45wc'
res = re.findall('\w',string)
print(res)

#6
raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"

res = re.findall(r'[\w\.-]+@[\w\.-]+',raw_text)
print(res)