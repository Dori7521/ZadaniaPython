#Dict comprehension

#1
from glob import escape


result = {i:i**2 for i in range(1,8)}
print(result)

#2
stocks = ['Playway', 'CD Projekt', 'Boombit']
result = {word:len(word) for word in stocks}
print(result)

#3
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result = {val:key for (key,val) in stocks.items()}
print(result)

#4
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:value for (key,value) in stocks.items() if value>100}
print(result)

#5
# result= [{i:i for i in range(1,10)},{i:i**2 for i in range(1,10)},{i:i**3 for i in range(1,10)}]
result2=[{i:i**j for i in range(1,10)} for j in range(1,4)]
print(result2)

#6
indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']

result={i:{key:None for key in properties} for i in indeks}
print(result)

#7
indeks = ['WIG20', 'mWIG40', 'sWIG80']

result = {i:indeks[i] for i in range(0,len(indeks))}
# result = {key: val for key, val in enumerate(indeks)}
print(result)
