# Instrukcja warunkowa

#1
filename = '01012020_sales.xlsx'

if filename.find('xlsx'):
    print('TAK')
else:
    print('NIE')

#2
code = 'DSVNDOICSN'
if code.isupper():
    print('TAK')
else:
    print('NIE')

#3
number = 1.0
if isinstance(number,int):
    print('TAK')
else:
    print('NIE')

#4
password = 'cskdnjcasa#!'
if len(password)>=11:
    print('Hasło poprawne')
else:
    print('Hasło zbyt krótkie')

#5
password = 'cskdnjcasa#!'
if password.find('!') and len(password)>=11:
    print('Hasło poprawne')
else:
    print('Hasło niepoprawne')

#6
project_ids = ['02134', '24253']
project_id = '02135'

if not project_id is project_ids:
    project_ids.append(project_id)
    
print(project_ids)

#7
project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02']=='new':
    project_ids['02']='open'

print(project_ids)

#8
item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove('001')

print(items)