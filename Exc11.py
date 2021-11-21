# Pętla for

#1
from typing import SupportsComplex


result=[]
for i in range(10,100):
   if i%11==0:
       result.append(str(i))

print(','.join(result))

#2 
result=[]
for i in range(10,100):
   if i%11==0 and i%3!=0:
       result.append(str(i))

print(','.join(result))

#3
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
new_items = []
for i in items:
    if i%2==0:
        new_items.append(i)

print(new_items)

#4
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for item in items:
    if not item in result:
        result.append(item)

print(result)

#5
result = []
text = 'Python jest bardzo popularnym językiem programowania'
text = text.lower()
text = text.split(' ')

for i in range(4):
    result.append(text[i]) 
print(result)

#6
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
results = []

for i in probabilities:
    if i > 0.5:
        results.append(i)
print(results)

#7
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
results = []

for prob in probabilities:
    if prob<0.5:
        results.append(0)
    elif prob >=0.5:
        results.append(1)

print(results)

#8
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
sumx = 0
sumy = 0
sumz = 0


sumx = items.count('x')
sumy = items.count('y')
sumz = items.count('z')

results = {'x': sumx,'y' : sumy,'z' : sumz}

print(results)

#8.1
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

freq = {}

for i in items:
    if i not in freq.keys():
        freq[i]=1
    else:
        freq[i]+=1

print(freq)


        

