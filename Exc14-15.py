#Input/Output

#1
with open('playway.txt', 'r') as file:
    lines = file.read().splitlines()

maxi = []

for idx,line in enumerate(lines):
    if idx>0:
        maxi.append(float(line.split(',')[2]))

avg = sum(maxi)/len(maxi)
print(f'Średnia maksymalnych wartosci z 3 dni: {avg:.2f}')

#2
with open('indeksy.txt', 'r') as file:
    lines = file.read().splitlines()

wig = []
results = [line for idx, line in enumerate(lines) if line.startswith('WIG')]
print(results)

# for idx, line in enumerate(lines):
#     if line.startswith('WIG'):
#         wig.append(line)

# print(f'Nazwy zaczynające się od WIG: {wig}')

#3
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

# data_dict = dict()
# list_date = list()
# list_close = list()

# for idx, line in enumerate(content):
#     if idx>0:
#         list_date.append(line.split(',')[0])
#         list_close.append(line.split(',')[4])

# data_dict['Data'] = list_date
# data_dict['Zamknięcie'] = list_close

# print(data_dict)

data = [(line.split(',')[0],line.split(',')[4]) for line in content]

data_dict = {
    data[0][0] : [data[1:][i][0] for i in range (len(data)-1)],
    data[0][1] : [float(data[1:][i][1]) for i in range (len(data)-1)]
}


print(data_dict)

#4
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

wol = [line.split(',')[-1] for line in content][1:]
wol = [int(w) for w in wol]
max_wol = max(wol)

print(f'Max Vol: {max_wol}')
print('-' * 20)

#5
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0],int(val[1])) for val in data]

max_vol = max(val[1] for val in data)
max_date = list(filter(lambda val : val[1]==max_vol, data))[0][0]
print(f'Data: {max_date}')
