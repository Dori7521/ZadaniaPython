#Input/Output

#1
# with open('num.txt', 'w') as file:
#     for i in range(2,19):
#         if i % 2 == 0:
#             print(i, file=file)

even_num = [i for i in range(2,20) if i%2 ==0]

with open('num.txt', 'w') as file:
    for num in even_num:
        file.write(str(num)+'\n')

#2
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    #json.dump(stocks,file,indient=4)
    json_stocks = json.dumps(stocks,indent=4)
    file.write(json_stocks)

#3
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv','w') as file:
        file.write(','.join(headers) + '\n')

        for user in users:
            file.write(','.join(user) + '\n')