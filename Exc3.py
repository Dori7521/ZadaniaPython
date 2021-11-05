import math
print(f'Dalsze roziwazywanie zadan')
#8
ax = 3
ay = 2
bx = -1
by =-1

odl = math.sqrt((ax+abs(bx))**2 + (ay+abs(by))**2)

print(f'Odległość punktów A i B wynosi: {odl}')

#9
a=1
b=5
c=4

delta = b**2 - 4*a*c              # mozna tez delta_sqrt = (delta)**(1/2)

x1 = (-b - math.sqrt(delta))/2*a  # x1 = (-b - delta_sqrt)/2*a
x2 =  (-b + math.sqrt(delta))/2*a

print(f'x1 = {x1} \nx2 = {x2}')