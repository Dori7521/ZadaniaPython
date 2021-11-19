# Pętla for

#1
result=[]
for i in range(10,100):
   if i%11==0:
       result.append(str(i))

print(','.join(result))

#2 
result=[]
for i in range(10,100):
   if i%11==0 and i%3!=0:
       result.append(str(i))

print(','.join(result))

#3
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
new_items = []
for i in items:
    if i%2==0:
        new_items.append(i)

print(new_items)

#4
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

result.append(items[0])
for item in items:
    if not item in result:
        result.append(item)

print(result)