#GENERATORY

#1
def file_gen(items):
    for item in items:
        if item.endswith('txt'):
            yield item


#2
def enum(items):
    i=0
    for item in items:
        yield tuple((i,item))
        i+=1

#print(list(enum(['TEN','CDR','BBT'])))

#3
def dayname(index):
    days = ['pon','wt','śr','czw','pt','sb','nd']
    yield days[index-1]
    yield days[index]
    yield days[(index+1)%7]


# for pair in dayname(0):
#     print(pair)



    