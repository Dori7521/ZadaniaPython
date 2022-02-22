#Moduły

#1
import calendar
from turtle import resetscreen
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

#7
text = 'Programowanie w języku Python - od A do Z'

lista = re.split(r'\s+',text)

print(lista)

#8

import string

print(string.ascii_letters)

#9
from collections import Counter

items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

print(Counter(items))

#10
import math

def sigmoid(x):
    return (1/(1+math.exp(-x)))

#11
import random

ziarno = random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']


print(random.choice(items))

#12
random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']

random.shuffle(items)

print(items)

#13
import pickle

ids=['001', '003', '011']

with open('data.pickle','wb') as file:    #write and binary
    pickle.dump(ids,file)

#14
import json

stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}

res = json.dumps(stocks,indent=4,sort_keys=True)
print(res)