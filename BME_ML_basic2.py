# BME_ML_basic2

# list methods
# append: adds an element at the end of the list
x = [1, 2, 3, 4, 5]
x.append(100) # An element 100 is added in the last index, and the list itself is updat
# append can add a single element (not multiple elements) (ex. x.append(10,20) --> erro
# If you append multiple elements, then you can try multiple append( ).
# Ex)
# x.append(10)
# x.append(20)
print("append(): ", x)

# pop: removes the element at the end of the list or at the specified index given the i
x = [1, 2, 3, 4, 5]
x.pop() # The last index element is removed (poped), and the list itself is updated.
# The removed (poped) value is returned.
print("pop(): ", x)
x = [1, 2, 3, 4, 5]
x.pop(1) # The 1st index is removed
print("pop(): ", x)

# extend: add the elements of a list to the end of the current list.
x = [1, 2, 3, 4, 5]
y = [10, 20]
x.append(y) # A list [10,20] is added in the last index, and the list itself is updated
( )
# "x.append(y)" is same as "x + y"
print("extend(): ", x)

# insert: adds an element at the specified position (before the index)
# insert(index, element)
x = [1, 2, 3, 4, 5]
x.insert(3, 0)
print("insert(): ", x)

# remove: removes the first item with the specified value
x = [1, 2, 3, 4, 5]
x.remove(2)
print("remove(): ", x)

# count
x = [1, 2, 3, 3, 4, 5]
print("count():", x.count(3)) # return value

# index
x = [1, 2, 3, 3, 4, 5]
print("index():", x.index(3)) # return value (from left to right)

# reverse: reverses the order of the list
x = [1, 2, 3, 4, 5]
x.reverse()
print("reverse():", x)

# sort: sort the elements
x = [4, 3, 1, 2, 5]
x.sort() # default: ascending order (reverse=False)
print("sort():", x)
x.sort(reverse=True) # descending order
print("sort():", x)

# clear: removes all the element in the list
x = [1, 2, 3, 4, 5]
x.clear()
print("clear():", x)

# copy
x = [1, 2, 3, 4, 5]
y = x.copy()
print("copy:", y)
print(id(x), id(y))

x = [1, 2, 3, 4, 5]
y = x
y[0] = 100
print(x, id(x))
print(y, id(x))
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print(x, id(x))
print(y, id(y))

# tuple methods
# there are only 2 methods: count(), index()
# count
x = (1, 2, 3, 3, 4, 5)
print("count():", x.count(3)) # return value

# index
x = (1, 2, 3, 3, 4, 5)
print("index():", x.index(3)) # return value (from left to right)


# dictionary methods
# clear
a = {"Math": 80, "English": 90, "Korean": 85}
print("clear():", a.clear())

# copy
a = {"Math": 80, "English": 90, "Korean": 85}
b = a.copy()
print("copy():", a.copy())
b["Math"] = 100
print("Original: ", a)
print("Copied and changed: ", b)
c = a # shares same memory
c["Math"] = 100
print("Original w/o copy: ", a) # original also changed
print("Assigned and changed: ", c)

# fromkeys: create a new dictionary with keys
x = ('Math', 'English', 'Korean') # a list is also OK
y = 0
a = dict.fromkeys(x, y) # creates a dictionary with keys and values
print("fromkeys():", a)

# get: returns the value for the specified key if the key is in a dictionary
a = {"Math": 80, "English": 90, "Korean": 85}
print("get():", a.get("Math")) # is same as "a["Math"]"
print(a.get("Physics")) # if the key is not in a dictionary, "None" is returned
#a["Physics"] # if the key is not in a dictionary, error

# items: returns an item object that displays a list of dictionary's tuple pairs.
a = {"Math": 80, "English": 90, "Korean": 85}
print("items():", a.items())

# pop: removes the item having a spedific key 
a = {"Math": 80, "English": 90, "Korean": 85}
a.pop("Math")
print("pop():", a)

# popitem: removes the item that was last inserted into the dictionary
a = {"Math": 80, "English": 90, "Korean": 85}
a.popitem()
print("popitem():", a)

# setdefault: add new item only
a = {"Math": 80, "English": 90, "Korean": 85}
a.setdefault("Physics", 60)
print("setdefault():", a)
a.setdefault("Math", 100) # If the key exists, the item has no effect.
print("setdefault():", a)

# update: add new items or update values
a = {"Math": 80, "English": 90, "Korean": 85}
a.update([("Math",100)])
print("update():", a)
a.update([("Physics",60)])
print("update():", a)
