# BME_ML_basic3

# logical statements
# if statement
# if some condition:
    # action
a = 1
b = 2
if a < b:
  a = a + 1

print(f"a is {a}")

# if / else
# if some condition:
#     action1
# else some condition:
#     action2
a = 1
b = 2
if a < b:
  a = a + 1
else:
  a = a - 1

print(f"a is {a}")

a = 1
b = 0
if a < b:
  a = a + 1
else:
  a = a - 1
  
print(f"a is {a}")

# if / elif / else
# if some condition:
#     action1
# elif some condition:
#     action2
# else some condition:
#     action3
a = 1
b = 2
if a < b:
  print("a is less than b")
elif a > b:
  print("a is greater than b")
else:
  print("a is equal to b")

a = 1
b = 0
if a < b:
  print("a is less than b")
elif a > b:
  print("a is greater than b")
else:
  print("a is equal to b")

a = 1
b = 1
if a < b:
  print("a is less than b")
elif a > b:
  print("a is greater than b")
else:
  print("a is equal to b")


# for loop statement
# for item_name in like_sequence:
    # action
for i in [1,2,3]:
  print(i)

my_list = [1,2,3]
for i in my_list:
  print(i)

my_tuple = (1,2,3)
for i in my_tuple:
  print(i)

my_number = [1,2,3,4,5,6,7,8,9,10]
for num in my_number:
  if num % 2 == 0:
    print(f"{num} is an even number")
  else:
    print(f"{num} is an odd number")

my_number = [1,2,3,4,5,6,7,8,9,10]
total_sum = 0
for num in my_number:
  total_sum = total_sum + num
print(f"The sum from 1 to 10 is {total_sum}")

my_friends = {'Mina', 'Roy', 'Pororo'}
for i in my_friends:
  print(i)

my_string = "Python is fun"
for letter in my_string:
  print(letter)

my_string = "Python is fun"
for letter in my_string:
  print(letter*3)

prices = {'apple':1000, 'orange':2000, 'banana':500}
for key in list(prices.keys()):
  if key == "orange":
    del prices[key]
print(prices)

prices = {'apple':1000, 'orange':2000, 'banana':500}
cnt = 0
for value in list(prices.values()):
  if value < 1500:
    cnt += 1 # cnt = cnt + 1
print(cnt)

my_string = "Machine learning is fun"
my_list = []
for i in my_string:
  my_list.append(i)
print(my_list)

a = {"Math":100, "English":90, "Korean":70}
for i,j in a.items():
  print(i,j)

# nested sequence (multiple elements)
# for nested_sequence in sequence:
    # action
pairs = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for (i, j) in pairs:
  print(i, j)

pairs = ([1,2,3], [4,5,6])
for (i, j, k) in pairs:
  print(i+j+k)

prices = {'apple':1000, 'orange':2000, 'banana':500}
my_basket = []
for (key, value) in list(prices.items()):
  if value < 1500:
    my_basket.append(key)

print(my_basket)

# for item_name in like_sequence:
#   for item_name in like_sequence:
#     action or statements
#   action or statements
x=[]
y=[]
for i in [1,2,3]:
  for j in [1,2,3]:
    x.append(i+j)
  y.append(i+j)
print(x)
print(y)

# while loop statement
# while only
# while some condtion:
#   action
x = 0
while x < 5:
  print(f"x is {x}")
  x += 1

# while / else
# while some condition:
#   action1
# else:
#   action2
x = 0
while x < 5:
  print(f"x is {x}")
  x += 1
else:
  print("This is the last action for a while loop")

# nested while loop
# while condition:
#   while condition:
#     action or statements
#   action or statements
x, y = [], [] # Pythonic style
i = 0
while i < 3:
  j = 0
  while j < 2:
    x.append(i+j)
    j += 1
  y.append(i+j)
  i += 1
print(x)
print(y)

# break, continue and pass
for letter in 'Python':
  if letter == 'h':
    break
  print(letter)

for letter in 'Python':
  if letter == 'h':
    continue
  print(letter)

for letter in 'Python':
    if letter == 'h':
      pass
    print(letter)

# switch statement
lang = "JavaScript"
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

my_score = 3
match my_score:
  case 0:
    my_grade = 'F'
  case 1:
    my_grade = 'D'
  case 2:
    my_grade = 'C'
  case 3:
    my_grade = 'B'
  case 4:
    my_grade = 'A'
  case _:
    my_grade = 'Not available'
print(f"My grade is {my_grade}")

# range()
# range(start, stop, step)
for i in range(1,10,2): # the last number is not included
  print(i)

for i in range(1,5): # step default = 1
  print(i)

for i in range(5): # one parameter is corresponding to the last number (not included). 
  print(i)

# enumerate
# enumerate(sequence)
my_list = [5,6,7,8,9]
for i in enumerate(my_list):
  print(i, type(i))

my_list = [5,6,7,8,9]
for i in enumerate(my_list, 100):
  print(i)

my_list = [5,6,7,8,9]
for i, j in enumerate(my_list):
  print(i, j)

# zip
# zip(sequence)
name = ['John', 'Pororo', 'Mina']
score = [100, 80, 90]
for item in zip(name, score):
  print(item)

name = ['John', 'Pororo', 'Mina']
score = [100, 80, 90]
for i, j in zip(name, score):
  print(i, j)

name = ['John', 'Pororo', 'Mina']
age = [34, 7, 22]
score = [100, 80, 90]
for i, j, k in zip(name, age, score):
  print(i, j, k)

# list comprehension
my_string = "hello"
my_list = [letter for letter in my_string]
print(my_list)

my_string = "hello"
my_list = []
for letter in my_string:
  my_list.append(letter)
print(my_list)

my_list = [x for x in 'word']
print(my_list)

my_list = [num for num in range(10)]
print(my_list)

my_list = [num*100 for num in range(10)]
print(my_list)

my_list = [num**2 for num in range(10) if num %2 == 0]
print(my_list)

my_list = []
for x in [1,2,3]:
  for y in [10,20,30]:
    my_list.append(x*y)
print(my_list)

my_list = []
for x in [1,2,3]:
  for y in [10,20,30]:
    if x*y > 20:
      my_list.append(x*y)    
print(my_list)

my_list = [x*y for x in [1,2,3] for y in [10,20,30] if x*y>20]
print(my_list)
