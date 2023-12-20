# BME_ML_basic5

# customized function

# def function_name(arguments)
#   function contents
def print3(x):
    print(x*3)
print3("Hello")

# two arguments
def print4(my_string, num):
    print(my_string * num)
print4(100, 200)

# keyword 'return'
# def function_name():
#     function contents
#     return xxx
def my_function(x,y,z):
    a = (x+y)*z
    return a
val = my_function(1,2,3)
print(val)

# dirctely
def my_function(x,y,z):
    return (x+y)*z
val = my_function(1,2,3)
print(val)

def cat_check(my_string):
    if 'cat' in my_string.lower():
        return True
    else:
        return False
print(cat_check("Cats are cute."))

# simple ver
def cat_check(my_string):
    return "cat" in my_string.lower()
print(cat_check("Cats are cute."))

# exercise 1
def strange_function(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return word + 'boy'
    else:
        return word[1:] + word[0] + 'girl'
print(strange_function("apple"))
print(strange_function("banana"))

# exercise 2
def my_func():
    print("Hello World")
print(my_func())

# exercise 3
def my_func(name):
    print("Hello " + name)
print(my_func('Yumi'))

# exercise 4
def my_func(x):
    if x == True:
        return "Hello"
    else:
        return "Good bye"
print(my_func(True))
print(my_func(False))

# exercise 5
def my_func(x,y,z):
    if z == True:
        return x
    else:
        return y
print(my_func(1,2,True))
print(my_func(1,2,False))

# exercise 6
def my_func(x,y):
    return x+y
print(my_func(3,5))

# exercise 7
def my_func(my_string):
    new_string = ""
    for index, character in enumerate(my_string):
        if index % 2 == 0:
         new_string += character.upper()
        else:
          new_string += character.lower()
    return new_string
print(my_func("apple"))
print(my_func("banana"))

# exercise 8
def my_func(my_list):
    for i in range(len(my_list)-1):
        if my_list[i:i+2] == [3,3]:
            return True
    return False
print(my_func([1,2,3,4,5]))
print(my_func([1,3,3,1]))

# exercise 9
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    else:
        if (11 in [a,b,c]) and (sum([a,b,c]) - 10 <= 21):
            return sum([a,b,c]) - 10
        else:
            return 'Bust'
print(blackjack(3,6,7))
print(blackjack(9,9,7))
print(blackjack(11,3,8))
print(blackjack(11,2,8))

# exercise 10
def sum_except6_9(my_list):
    total = 0
    add = True

    for num in my_list:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print(sum_except6_9([3,6,7]))
print(sum_except6_9([3,6,7,9]))
print(sum_except6_9([3,6,7,9,8]))
print(sum_except6_9([11,6,9,1]))

# exercise 11
def game007(my_list):
    target = [0,0,7]
    for num in my_list:
        if num == target[0]:
            target.pop(0)
            if len(target)==0:
                break
    return len(target)==0
print(game007([0,0,7,5]))
print(game007([0,0,5,7]))
print(game007([7,0,0,5]))

# exercise 12
def count_primes(num):
    # check the number 1
    if num < 2:
        return 0
    # the number 2 or greater
    primes = [2] # store a prime number 2
    x = 3
    while x <= num:
    # check if x is a prime number
        for y in primes:
            if x % y == 0:
                x += 2
                break
            else:
                primes.append(x)
                x += 2
    return len(primes)
print(count_primes(2))

# function arguments
# default values
def min_abs(a,b,c=0):
    return abs(min(a,b,c))
print(min_abs(1,2))
print(min_abs(1,2,-10))

def sum_multiply(a,b=10,c=1):
    return (a+b)*c
print(sum_multiply(10))
print(sum_multiply(10,1))
print(sum_multiply(10,1,2))

def cal_BMI(weight, height):
    return weight/height**2
print(cal_BMI(80, 1.7))
print(cal_BMI(height=1.7, weight=80))

# function arguments
# *args and **kwargs
def student_diff(a,b,c,d,e,f,g):
    return max(a,b,c,e,d,f,g) - min(a,b,c,e,d,f,g)
print(student_diff(50,60,70,80,90,100,50))

# def function name(*args):
def student_diff(*args):
    return max(args) - min(args)
print(student_diff(50,60,70,80,90,100,50))
print(student_diff(50,60,70,80,90,100,50,40))
print(student_diff(50,60,70))
def student_diff(*args):
    print(args, type(args))
    return max(args) - min(args)
print(student_diff(10,20))
def student_diff(*hotdog):
    return max(hotdog) - min(hotdog)
print(student_diff(50,60,70,80,90,100,50))

# def function names(**kwargs):
def my_func(**kwargs):
    print(kwargs, type(kwargs))
print(my_func(fruit="apple", vegetable="lettuce"))
print(my_func(height=1.7, weight=80, age=20))

def myfunc(*args, **kwargs):
    print(f"The argument is {args}")
    print(f"The keyword argument is {kwargs}")
print(myfunc(10,20,30, age=20, height=1.7, weight=80))

# local and global variables
def my_thought():
    s = "I hate Python class"
    print(s)
s = "I love Python class"
print(my_thought())

def my_thought():
    s = "I hate Python class"
    print(s)
s = "I love Python class"
print(my_thought())
print(s)

def my_thought():
    global s
    s = "I hate Python class"
    print(s)
s = "I love Python class"
print(my_thought())
print(s)

# some useful functions
# map function
def sq_func(x):
    return x**2
print(sq_func(3))
print(map(sq_func, [1,2,3]))
print(list(map(sq_func, [1,2,3])))
for i in map(sq_func, [1,2,3]):
    print(i)
# filter function
def odd_even(my_number):
    return my_number % 2 == 0
print(odd_even(2))
print(odd_even(3))
print(list(filter(odd_even, [1,2,3,4,5,6])))
# lambda function
def my_func(my_string):
    return my_string[0].isupper()
print(my_func("Abc"))
print(lambda my_string: my_string[0].isupper())
print(list(filter(lambda my_string: my_string[0].isupper(), ["Hello", 'boy', 'Great'])))
print(list(filter(lambda my_number: my_number%2==0, [3,4,5,6,7])))
print(list(map(lambda x: x[::-1], ["Hello", 'boy', 'Great'])))
# literator
my_tuple = ("images1", "images2", "images3")
t_iterator = iter(my_tuple)
print(type(t_iterator))
print(next(t_iterator))
print(next(t_iterator))
print(next(t_iterator))
my_list = ["videos1", "videos2", "videos3"]
l_iterator = iter(my_list)
print(type(l_iterator))
print(next(l_iterator))
print(next(l_iterator))
print(next(l_iterator))
# iterator for loop
my_tuple = ("images1", "images2", "images3")
t_iterator = iter(my_tuple)
for i in t_iterator:
    print(i)
my_list = ["videos1", "videos2", "videos3"]
l_iterator = iter(my_list)
for i in l_iterator:
    print(i)


# generator : yield vs return
def even_numbers(n):
    results = []
    for x in range(n):
        if (x % 2 == 0):
            results.append(x)
    return results
num = even_numbers(10)
print(num)

def my_func():
    return 100
    print("Can you see me?")
    print("Can you really see me?")
    print("You can't?")
print(my_func())

# yield
def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x
num = even_numbers(10)
print(num)
print(type(num))
print(list(num))

def even_numbers(n):
    for x in range(n):
        if (x % 2 == 0):
            yield x
num = even_numbers(10)
print(next(num))
print("even_numbers function is not finished.")
print("I can do another job using the first result.")
print(next(num))
print("even_numbers function is not finished.")
print("I can do another job using the second result.")
print(next(num))
print("even_numbers function is not finished.")
print("I can do another job using the third result.")
print(next(num))
print("even_numbers function is not finished.")
print("I can do another job using the fourth result.")
print(next(num))
print("Now, even_number function is finished.")
print("No more next(num). With next(num), you will have an error.")
print("If you convert num to a list....")
print(list(num))




