#1
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

result = bool
for i in list1:
    if i in list2:
        result=True
        break
    else:
        result=False
        break
print(result)


#2
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = bool

for item in hashtags:
    if isinstance(hashtags,str):
        result = True
    else:
        result = False

print(result)