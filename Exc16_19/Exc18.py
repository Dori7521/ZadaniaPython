#LAMBDA

#1
stocks = ['playway', 'boombit', 'cd projekt']

results = list(map(lambda word : len(word), stocks))
print(results)

#2
def sort_list(list):
    return sorted(list,key = lambda n: n[1])

#3
func_2 = lambda x,y : x+y+2

#4
items = [(3, 4), (2, 5), (1, 4), (6, 1)]

items.sort(key = lambda item: item[0]**2 + item[1]**2)
#print(items)

#5
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks.sort(key= lambda price: price['price'])
#print(stocks)

#6
results = list(filter(lambda name :name['indeks']=='mWIG40', stocks))
#print(results)

#7
tof = list(map(lambda word: word['indeks']=='mWIG40',stocks))
#print(tof)

#8
items = ['P-1', 'R-2', 'D-4', 'F-6']
result = list(map(lambda x: x.replace('-',''),items))
#print(result)

#9
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

result = list(map(lambda a,b : a%b,num1,num2))
#print(result)