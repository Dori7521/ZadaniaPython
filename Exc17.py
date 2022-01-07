# Definiowanie funkcji

#1
def maximum(a,b):
    if a > b:
        return a
    else:
        return b

#2
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

#3
def multi(numbers):
    multiple = 1
    #   for number in numbers:
    #   multiple *= number

    for i in range(len(numbers)):
        multiple*=numbers[i]
    return multiple

#4
def map_longest(words):
    longest = 0
    for word in words:
        if longest > len(word):
            continue
        else:
            longest = len(word)

        return longest

#  length = []
#     for word in words:
#         length.append(len(word))
#     return max(length)

#5
def filter_ge_6(words):
    list_of_words = []
    for word in words:
        if len(word)<6:
            continue
        else:
            list_of_words.append(word)
    return list_of_words

#6
def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)

#7
def count_str(things):
    count = []
    for thing in things:
        if isinstance(thing,str):
            count.append(thing)
    return len(count)


#8
def count_str(things):
    count = []
    for thing in things:
        if isinstance(thing,str) and len(thing)>2:
            count.append(thing)
    return len(count)

#9
def remove_duplicates(items):
    new_items = []
    for item in items:
        if item in new_items:
            continue
        else:
            new_items.append(item)
    return new_items

# def remove_duplicates(items):
#     return list(set(items))

#10
def is_distinct(items):
    return len(items)==len(set(items))

#11  ZAJEBIOZA ZADANIE 
def function(idx, l=[]):                        # przy trzecim wywołaniu funkcji, lista jest nadpisywana [0, 1, 8, 0, 1, 8, 27, 64, 125]
    for i in range(idx):
        l.append(i ** 3)
    print(l)

# def function(idx, l=None):                    w tym przypadku lista przy każdym wywoływaniu funkcji będzie tworzona na nowo [0, 1, 8, 27, 64, 125]
#     if l is None:
#         l = []
#     for i in range(idx):
#         l.append(i ** 3)
#     print(l)
 
# function(3)
# function(5, ['a', 'b', 'c'])
# function(6)

print(function(3))
print(function(5,['a','b','c']))        # jeśli jest podawany idx i lista, tworzona jest nowa lista ZAWSZE (nie nadpisuje się)
print(function(6))

#11
def function(*args, **kwargs):
    print(args, kwargs)

function(3,4)                    # (3, 4) {}
function(x=3,y=4)                # () {'x': 3, 'y': 4}
function(1,2,x=3,y=4)            # (1, 2) {'x': 3, 'y': 4}

#12
def is_palindrome(word):
    word = list(word)
    palindrome = list(word)
    palindrome.reverse()
    return word == palindrome

# def is_palindrome(string):
#     inverse = string[::-1]
#     return True if string == inverse else False











    

