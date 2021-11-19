# LISTY

#1
cities = ['Warszawa','Łódź','Kraków']
cities.append('Gdańsk')
print(cities)

#2
idx = ['001', '002', '001', '003', '001']
num = idx.count('001')
print(f'Liczba wystąpień: {num}')

#3
text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę','e')
text =text.replace(' ','')
text.split()
zb = set(text)
fin = list(sorted(zb))
print(fin[:10])

#4
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0,'phone.jpg')
filenames.remove('ball.png')
print(filenames)

#5
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']

day1.extend(day2)           #nie przyrównywać do innej zmiennej!!!!!!!!
print(day1)

#6
techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)

#7
hashtags = ['summer', 'time', 'vibes']
joining = '#'.join(hashtags)
print('#'+joining)