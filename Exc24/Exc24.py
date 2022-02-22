#Exercises

#1
y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

def accuracy(y_true,y_pred):
    counter = 0

    for i,j in zip(y_pred,y_true):
        if i==j:
            counter+=1

    return round(counter/len(y_true),4)

print(accuracy(y_true,y_pred))

#2
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2,10.4,10.8,11.0]
result =[]
def mae(y_true,y_pred):
    for i,j in zip(y_true,y_pred):
        mae=(abs(i-j)/len(y_true))
        result.append(mae)
        
        # result=[abs(i[1]-i[0] for i in zip(y_true,y_pred))]

    return round(sum(result),3)

print(mae(y_true,y_true))


#3
def mse(y_true,y_pred):
    errors = [((i[1]-i[0])**2)/len(y_true) for i in zip(y_true,y_pred)]
    return round(sum(errors),3)

print(mse(y_true,y_pred))

#4
x=5

def relu(x):
    result=max(x,0)
    return result

#5
items = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# result=[]

def flatten(items):
    # for i in items:
    #     for j in i:
    #         result.append(j)
    result = [j for i in items for j in i]
    return result

#6

x=[1,2,3,4,0,0,3,4,5,0,0]

def transfer_zeros(x):
    res = [i for i in x if i!=0]
    zeros=[j for j in x if j==0]
    res+=zeros
    return res


# def transfer_zeros(items):
#     result = []
#     counter = 0
#     for item in items:
#         if item == 0:
#             counter += 1
#         else:
#             result.append(item)
#     result.extend([0] * counter)
#     return result


#7
x = [0,3]
y = [4,0]

def euclidean_distance(x,y):
    result = [(i[1]-i[0])**2 for i in zip(x,y)]
    return (sum(result))**0.5

#8
def arange(start, stop, step=1):
    lista=[i for i in range(start,stop,step)]
    return lista

#9
l1=[[1],[2]]
l2=[[3],[4]]

def concat(l1,l2):
    # result = [[i[0][0],i[1][0]] for i in zip(l1,l2)]
    result=[[i[0],j[0]] for (i,j) in zip(l1,l2)]
    return result

#10 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def identity(x):
    array = [[0]*x for i in range(x)]
    for idx, item in enumerate(array):
        item[idx]=1
    # print(list(enumerate(array)))
    return array

print(identity(3))

#11
def fill_value(height,width,value):
    array = [[value]*width for i in range(height)]
    return array

#12

def trace(x):
    result=0
    # array=[[x] for i in range(x)]
    for idx,item in enumerate(x):
        result+=item[idx]
    return result

print(trace([[1,2,3],[4,2,3],[3,2,1]]))




