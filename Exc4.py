# Operator wycinania

#1
filename = 'view.jpg'
print(filename [-3:])

#2
text = 'PKV-89415-PLN'
print(text [:3]+text[-3:])

#3
string = '1 0 0 1 0 1'
binary_string = string[::2]
number = int(binary_string, 2)
print(f'Znaleziona liczba: {number}')

#4
text = 'Kurs Python'
print(text[::-1])