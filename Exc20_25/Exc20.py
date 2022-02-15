#set comprehension

#1
from distutils.file_util import move_file


omega = {(i,j) for i in range(1,7) for j in range(1,7)}
result = {prob for prob in omega if prob[0]+prob[1]>10}
print(f'P-stwo: {len(result)/len(omega):.2f}')

#2
desc = "Playway: Playway to producent gier komputerowych."
text = desc.lower().replace(':','').replace('.','').split()
result = {word for word in text}
print(len(result))

#3
omega = {(i,j) for i in range(1,7) for j in range(1,7)}
result = {sq for sq in omega if (sq[0]**2+sq[1]**2)>=45}
print(f'P-stwo: {len(result)/len(omega):.2f}')

#4
omega = {(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)}
result = {modulo for modulo in omega if (modulo[0]+modulo[1]+modulo[2])%7==0}
print(f'P-stwo: {len(result)/len(omega):.2f}')

#5
omega = {(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)}
result = {modulo for modulo in omega if (modulo[0]**2+modulo[1]**2+modulo[2]**2)%3==0}
print(f'P-stwo: {len(result)/len(omega):.4f}')

#6
omega = {(i,j,k) for i in range(1,7) for j in range(1,7) for k in range(1,7)}
result = {modulo for modulo in omega if modulo[0]%2!=0 and modulo[1]%2!=0 and modulo[2]%2!=0}
print(f'P-stwo: {len(result)/len(omega):.3f}')