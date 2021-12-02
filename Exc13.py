#while

prime = []
number = 2
first = 0

while first < 10:
    for i in range(2,number):
        if number%i==0:
            break
    else:
        prime.append(str(number))
        first+=1
    number+=1
print(','.join(prime))