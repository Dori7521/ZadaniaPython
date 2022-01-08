#TUPLE

#1
wig20 =('CDR','PKO','PEO')
mwig40 = ('PLW','AMC','BFT')

sum = wig20.__add__(mwig40)   # sum = wig20 + mwig40
print(sum)

#2
res = (wig20,mwig40)
print(res)

#3
members = (('Kasia',23),('Tomek',19))
an_mem = ('Adam',26)
wh_mem = (members[0],an_mem,members[1])
print(wh_mem)

#4
default = ('YES', 'NO', 'NO', 'YES', 'NO')

num = default.count('YES')
print(f'Liczba wystąpień: {num}')

#5
names = ('Monika','Tomek','Adam','Olaf')
sorts = tuple(sorted(names))                         # przy sortowaniu trzeba dać TUPLE!
print(sorts)

#6
info = (('Monika',19),('Tomek',21),('Adam',18),('Jarek',30))
rosn = tuple(sorted(info,key=lambda item:item[1] ))
male = tuple(sorted(info,key=lambda item:item[1],reverse=True))

print(f'Rosnąco: {rosn}')
print(f'Malejąco: {male}')

#7
stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))

print(stocks[0][1][0])