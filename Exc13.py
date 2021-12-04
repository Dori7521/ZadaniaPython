# pętla while

#1
hmuch = 0
number = 2
prime = []

while hmuch <10:
    for i in range(2,number):
        if number%i==0:
            break
    else:
        prime.append(str(number))
        hmuch+=1
    number+=1

print(','.join(prime))

# while hmuch<10:                                                for else i number+=1 są w jednej linii !!!!!!!!
#     for i in range(2,number):                                 dla number = 2 nie znajduje iteracji i idzie do else
#         if number%i==0:                                       number = 6   6 dzieli 2 ->od razu zachodzi break pętli (nie jest pierwsza) i idzie dalej (number+=1)                                                              
#             print(f'{number} is not a prime number!')         number = 5  5 nie dzieli 2,3,4 -> idzie do else i wykonuje tamtejsze poelcenia
#             break
#     else:
#         print(f'{number} is a prime number :)') 
#         hmuch+=1
#     number+=1   

#2
n = 1
pv = 1000
r = 0.04
fv = pv*(1+r)

while fv<=2000:
    fv = fv*(1+r)
    n+=1

print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat.')

#3
max_iters = 10000 
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size >precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate*derivative(w_prev)
    previous_step_size = abs(w_0-w_prev)
    iters+=1
print(f'Minimum lokalne w punkcie: {w_0:.2f}')

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start+end)/2)

    if numbers[mid]==target:
        flag = True
        break
    else:
        if numbers[mid]<target:
            start = mid+1
        else:
            end = mid -1 

if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')


