# INPUT/OUTPUT

#0.1
with open('data.txt','r') as file:
    # for line in file:                                 odczyta
    #     print(line,end = '')

    lines = file.readlines()                        # odczyta jako lista
    print(lines)

#0.2
techs = ['python','java','sql','sas']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)

#0.3
with open('tree.txt','w') as file:
    for j in range(2):   
        for i in range(10):    
            print('{:>9}'.format('*'*i),end = '',file=file)
            print('{}'.format('*'*i),file=file)

#1

with open('playway.txt', 'r') as file:
    lines = file.read().splitlines()

close = []

for idx, line in enumerate(lines):
    if idx >0:
        close.append(int(line.split(',')[-2]))

close_avg = sum(close)/len(close)
print(f'3-dniowa srednia cena zamkniecia: {close_avg:.2f}')

#2
with open('indeksy.txt','r') as file:
    line = file.read().splitlines()
# -----------------------------------
result = []
for name in line:
    if name.startswith('WIG'):
        result.append(name)

print(result)

# indexes = [index for index in lines if index.startswith('WIG)]
# print(indexes)

#3
with open('plw_d.csv','r') as file:
    content = file.read().splitlines()
    
# data = [(line.split(',')[0],line.split(',')[4]) for line in content]

# result = {
#     data[0][0] : [data[1:][i][0] for i in range(len(data)-1)],
#     data[0][1] : [float(data[1:][i][1]) for j in range(len(data)-1)]
# }

# print(result)

data_dict = dict()
list1 = list()
list2 = list()

for idx, line in enumerate(content):
    if idx>0:
        list1.append(line.split(',')[0])
        list2.append(float(line.split(',')[4]))

data_dict['Data']=list1
data_dict['Zamkniecie'] = list2

print(data_dict)

#4
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

wol = []

for idx, line in enumerate(content):
    if idx > 0:
        wol.append(int(line.split(',')[-1]))


max_val = max(wol)                

# for value in wol:
#     if max_val>=value:
#         continue
#     else:
#         max_val = value

print(f'Max Vol: {max_val}')


#5
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0],int(val[1])) for val in data]

max_vol = max(val[1] for val in data)
max_date = list(filter(lambda val : val[1]==max_vol, data))[0][0]
print(f'Data: {max_date}')