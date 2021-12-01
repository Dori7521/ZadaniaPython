# Pętla for

# #1
# from typing import SupportsComplex


# result=[]
# for i in range(10,100):
#    if i%11==0:
#        result.append(str(i))

# print(','.join(result))

# #2 
# result=[]
# for i in range(10,100):
#    if i%11==0 and i%3!=0:
#        result.append(str(i))

# print(','.join(result))

# #3
# items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
# new_items = []
# for i in items:
#     if i%2==0:
#         new_items.append(i)

# print(new_items)

# #4
# items = [1, 5, 3, 2, 2, 4, 2, 4]
# result = []

# for item in items:
#     if not item in result:
#         result.append(item)

# print(result)

# #5
# result = []
# text = 'Python jest bardzo popularnym językiem programowania'
# text = text.lower()
# text = text.split(' ')

# for i in range(4):
#     result.append(text[i]) 
# print(result)

# #6
# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
# results = []

# for i in probabilities:
#     if i > 0.5:
#         results.append(i)
# print(results)

# #7
# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
# results = []

# for prob in probabilities:
#     if prob<0.5:
#         results.append(0)
#     elif prob >=0.5:
#         results.append(1)

# print(results)

# #8
# """
#     items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
#     sumx = 0
#     sumy = 0
#     sumz = 0

#     sumx = items.count('x')
#     sumy = items.count('y')
#     sumz = items.count('z')

#     results = {'x': sumx,'y' : sumy,'z' : sumz}

#     print(results)
# """
# #8.1
# items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

# freq = {}

# for i in items:
#     if i not in freq.keys():
#         freq[i]=1
#     else:
#         freq[i]+=1

# print(freq)

# #11
# text = """Python – język programowania wysokiego poziomu
# ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
# standardowych, którego ideą przewodnią jest czytelność i
# klarowność kodu źródłowego."""
# words = text.split()
# words = [word.lower() for word in words]
# words = [word.replace('.', '').replace(',', '') for word in words]
# words = [word for word in words if len(word) > 10]
# print(words)

# #12
# indexes = [
#     'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 
#     'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
#     'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
#     'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
#     'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
#     'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
#     'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
#     'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
# ]
# result = []
# for i in indexes:
#     if '20' in i or '30' in i:
#         result.append(i)

# print(result)

# #13
# gaming = {
#     '11B': 362.5,
#     'CDR': 297.0,
#     'CIG': 0.85,
#     'PLW': 318.0,
#     'TEN': 300.0
# }

# for ticker, close in gaming.items():
#     if close > 100.0:
#         print(ticker)


# #14
# names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
# for name in names:
#     if name.isalpha():
#         print(f'Hello {name}!')


#1.1
numbers = []
for i in range(14,100):
    if i%7==0:
        numbers.append(str(i))

print(', '.join(numbers))

#1.2
results = []
for i in range(11,100):
    if i%11==0 and i%3!=0:
        results.append(str(i))

print(','.join(results))

#1.3
items = [1,3,4,5,6,9,10,17,23,24]
items2 =[]

for i in items:
    if not i%2!=0:
        items2.append(i)

print(items2)

#1.4
items = [1,2,2,6,7,6,9]
results = []

for i in items:
    if not i in results:
        results.append(i)

print(results)

#1.5
text = 'Bardzo chce umiec programowac w Pythonie, ale czasami mi nie idzie.'
text = text.lower()
text = text.split(' ')
results = []
    
for t in text[:4]:
        results.append(t)
    
print(results)

#1.6
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
probs2 = []

for prb in probabilities:
    if prb>0.5:
        probs2.append(prb)

print(probs2)

#1.7
results = []

for p in probabilities:
    if p<0.5:
        results.append(0)
    else:
        results.append(1)

print(results)

#1.8
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
ditems={}

for item in items:
    if item not in ditems.keys():
        ditems[item]=1
    else:
        ditems[item]+=1

print(ditems)

#1.8.2
names = ['Jolka','Kaska','Monika','Jolka','Monika','Marta','Marta']
dnames = {}
for name in names:
    if name not in dnames.keys():
        dnames[name]=1
    else:
        dnames[name]+=1

print(dnames)

#1.9
text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
text = text.lower()
text = text.replace('–',' ')
text = text.replace('.',' ')
text = text.replace(',',' ')
text = text.split()

ltext = []

for t in text:
    if len(t)>10:
        ltext.append(t)

print(ltext)

#1.10
indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
]

for index in indexes:
    if '20' in index or '30' in index:
        print(index)


#1.11
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for key in gaming:
    if gaming[key]>100:
        print(key)

# for ticker, close in gain.items():
#       if close>100:
#           print(ticker)

#1.12
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')