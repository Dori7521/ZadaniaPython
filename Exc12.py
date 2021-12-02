#1
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

result = False 
for i in list1:
    if i in list2:
        result = True
        break

print(result)

#2
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
for h in hashtags:
    if not isinstance(h,str):
        result=False
        break
print(result)

#3
number = 13

if number>1:
    for i in range(2,number):
        if number%i!=0:
            print(f'{number} - liczba pierwsza')
            break
        else:
            print(f'{number} - nie liczba pierwsza')
            break
else:
    print(f'{number} - nie liczba pierwsza')

#4
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}


for ticker,info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0]*=4.0
    info[1] ='PLN'
        
    

print(gaming)