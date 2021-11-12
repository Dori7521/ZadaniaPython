#ZBIORY

#1
przedmioty ={'matematyka','polski'}
przedmioty.add('angielski')
print(przedmioty)

#2
text = 'Programming in python.'
vowels={'a','e','i','o','u'}
text = text.replace('.','')
text = text.replace(' ','')
letters = set(text.lower())

nset = letters.difference(vowels)                           # difference -> usuwa elementy jedengo zbioru z drugiego
print(f'Liczba elementów: {len(nset)}')

#3
A = {2,4,6,8}
B={4,10}

sym_diff =A.symmetric_difference(B)
print(f'Różnica symetryczna: {sym_diff}')

#4
ad1_id ={'001','002','003'}
ad2_id ={'002','003','007'}

sym_diff2 = ad1_id.symmetric_difference(ad2_id)           # symetric_difference -> pokazuje wszystkie elementy oprócz wspólnych (usuwa elementy wspólne)
print(f'Wybrane ID: {sym_diff2}')

#5
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

is_cb = is_clicked.intersection(is_bought)

print(f'ID klientow: {is_cb}')


#1.1
movies = {'Iron Man','Avengers','Dr. Strange'}
movies.add('Hulk')
print(movies)

#2.1
text = 'Programowanie jest Superanckie.'
randomls={'e','a','g'}
text.replace(' ','')
text.replace('.','')
letters = set(text.lower())
number = len(letters.difference(randomls))
print(number)

#3.1
A={1,3,5,7,10}
B={2,4,6,8,10}

sym_diff3 = A.symmetric_difference(B)
print(sym_diff3)

#4.1
ad1_ID = {'123','456','789'}
ad2_ID = {'456','789','901'}

sym_diff4 = ad1_ID.symmetric_difference(ad2_ID)
print(sym_diff4)

#5.1

is_c = {'135','157','179'}
is_b = {'123','135','245'}
 
is_cb1 =is_c.intersection(is_b)           # itersection - > pokazuje elementy wspólne zbiorów
print(is_cb1)

