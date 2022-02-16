#List comprehension

#1
with open('gaming.txt','r') as file:
    text=file.readlines()

text1 = [word.replace('\n','') for word in text]
text2 = [word for word in text1 if len(word)>0]
print(text2)

#2
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]

brutto = [round(price*(1+tax),2) for price in net_price]
print(brutto)

#3
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

fv = [round(pv*(1+r)**n,2) for r in rate]
print(fv)

#4
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

fv = [pv*(1+r)**n for r in rate]
interest=[round(fvs-pv,2) for fvs in fv]
print(interest)

#5
with open('plw.txt','r') as file:
    lines=file.read().splitlines()

text = [line.split() for line in lines if len(line)>0]
print(text)

#6
with open('plw.txt','r') as file:
    lines = file.read()

lines = lines.lower()
lines = lines.replace('\n',' ').replace(',',' ').replace('.',' ').split()
lines.sort()
text = [word for word in lines if len(word)>=8]
print(text)

#7
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))

result = [[key,value] for (key,value) in data.items()]
print(result)