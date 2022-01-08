#Funkcje wbudowane

#1
x = -1.5
expression = 'x**2 + x'
print(eval(expression))

#2
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1,tuple))
print(isinstance(var2,tuple))
print(isinstance(var3,tuple))
print(isinstance(var4,tuple))
print(isinstance(var5,tuple))

#3
characters = ['k', 'b', 'c', 'j', 'z', 'w']
#characters.sort()
print(f'Pierwsza: {min(characters)}')
print(f'Ostatnia: {max(characters)}')

#4
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

print(list(zip(ticker,full_name)))

#5
items = (' ', '0', 0.1, True)
print(all(items))

#6
items = ('', 0.0, 0, False)
print(any(items))

#7
number = 234
binary = bin(number)
#binary = binary[2:]
print(binary.count('1'))

