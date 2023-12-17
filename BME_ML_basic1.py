# BME_ML_python_basic_1

#basic methods
# capitalize: First upper case, the others lower cases
x = "machine learning is FUN"
print("captitalize(): ", x.capitalize())

# casefold: All lower cases
x = "machine learning is FUN"
print("casefold(): ", x.casefold())

# center: center
x = "machine learning is FUN"
print("center(): ", x.center(50)) # a total width
print("center(): ", x.center(50,'*')) # padding with *

# count: count a spedific character
x = "machine learning is FUN"
print("count(): ", x.count('i'))

# encode: encoding
x = "machine learning is FUN"
print("encode(): ", x.encode('ASCII'))
print("encode(): ", x.encode('UTF-8')) # Unicode Transformation Format (default)
print("encode(): ", x.encode('UTF-16'))
print("encode(): ", x.encode('UTF-32'))

# endswith: Does it end with xxx? True or False
x = "machine learning is FUN"
print("endswith(): ", x.endswith('FUN'))
print("endswith(): ", x.endswith('fun'))

# expandtabs: set up the tab space size
x = "machine\tlearning\tis\tFUN" # \t is a tab space (default space size: 8)
print(x)
print("expandtabs(): ", x.expandtabs(4))

# find: return the index of a specific character from the left
x = "machine learning is FUN"
print("find(): ", x.find('e')) # the lowest index (from the left)
print("find(): ", x.find('FUN'))
print("find(): ", x.find('fun')) #No found, it returns -1

# rfind: return the index of a specific character from the right
x = "machine learning is FUN"
print("rfind(): ", x.rfind('e')) # the highest index (from the right)
print("rfind(): ", x.rfind('FUN'))
print("rfind(): ", x.rfind('fun')) #No found, it returns -1

# index: find the index of a specific character
x = "machine learning is FUN"
print("index(): ", x.index('e')) # the lowest index (from the left)
print("index(): ", x.index('FUN'))
#print("index(): ", x.index('fun')) # No found, it gives an error

# rindex: find the index of a specific character from the right
x = "machine learning is FUN"
print("rindex(): ", x.rindex('e')) # the highest index (from the right)
print("rindex(): ", x.rindex('FUN'))
#print("rindex(): ", x.rindex('fun')) # No found, it gives an error

# format
feel = 'happy'
print("format(): ", "John is {}".format(feel))

# isalnum: return True if all characters in the string are alphanumeric (alphabet or nu
x = "Machine Learning Is Fun"
print("isalnum(): ", x.isalnum()) # False because of the space
y = "MachineLearningIsFun"
print("isalnum(): ", y.isalnum()) # True

# isalpha: return True if all characters in the string are alphabet
x = "Machine Learning Is Fun"
print("isalpha(): ", x.isalpha()) # False because of the space
y = "MachineLearningIsFun"
print("isalpha(): ", y.isalpha()) # True

# isascii: return True if all characters in the string are ascii characters
# ASCII is a 7-bit character set containing 128 characters.
# It contains the numbers from 0-9, the upper and lower case English letters from A to 
# and some special characters in a keyboard (!@#$%^&*()+'";:<>?)
x = "Machine Learning Is Fun"
print("isascii(): ", x.isascii()) # True
y = "머신러닝"
print("isascii(): ", y.isascii()) # False

# isdecimal: return True if all characters in the string are decimals
x = "Machine Learning Is Fun"
print("isdecimal(): ", x.isdecimal()) # False
y = "123"
print("isdecimal(): ", y.isdecimal()) # True

# isdigit: return True if all characters in the string are degits
x = "Machine Learning Is Fun"
print("isdigit(): ", x.isdigit())

# isnemeric: return True if all characters in the string are numeric
x = "Machine Learning Is Fun"
print("isnumeric(): ", x.isnumeric())

# isidentifier: return True if all characters in the string are identifier
x = "Machine Learning Is Fun"
print("isidentifier(): ", x.isidentifier())
y = "Machine_learning"
print("isidentifier(): ", y.isidentifier())

# isprintable: return True if all characters in the string are printable
# 1) A string contains only alphanumeric or underscores(_).
# 2) A string does not start with a number
# 3) A string does not contain any spaces
x = "Machine Learning Is Fun"
print("isprintable(): ", x.isprintable())
y = "Machine\tlearning"
print("isprintable(): ", y.isprintable())

# isspace: return True if all characters in the string are spaces
x = "Machine Learning Is Fun"
print("isspace(): ", x.isspace())
y = "         "
print("isspace(): ", y.isspace())

# istitle: return True if the string follows the rules of a title
# The first character of each word is uppercase, and others are lowercase
print("istitle(): ", x.istitle())
y = "Machine Learning Is Fun"
print("istitle(): ", y.istitle())

# isupper: return True if all characters in the string are uppercase
x = "Machine Learning Is Fun"
print("isupper(): ", x.isupper())

# islower: return True if all characters in the string are lowercase
x = "Machine Learning Is Fun"
print("islower(): ", x.islower())

# join: convert the elements of an iterable into a string with a separator
# Here, an iterable indicate that a single variable includes multiple values (list, str
# An elemenet of a string is each character.
# seperator.join(string)
my_string = "Hello Machine Learning"
print("join(): ", '*'.join(my_string))
print("join(): ", ' '.join(my_string))
# when an iterable is a list: seperator.join(list)
my_list = ["Hello", "Machine", "Learning"]
print("join(): ", '*'.join(my_list))
print("join(): ", ' '.join(my_list))

# ljust: return a left justified version of the string
# string.ljust(length, character)
# It sets the string length, and moves the string to the left. The others will be padde
print("ljust(): ", x.ljust(50, "*")) # padding with *
print("ljust(): ", x.ljust(50)) # No padding

# rjust: return a right justified version of the string
# string.rjust(length, character)
# It sets the string length, and moves the string to the right. The others will be padd
print("rjust(): ", x.rjust(50, "*")) # padding with *
print("rjust(): ", x.rjust(50)) # No padding

# lstrip: return stripped (trimmed) string in the left side
# string.lstrip(removed characters)
y = "****////Machine learning is fun///***"
print("lstrip(): ", y.lstrip("*/")) # * or / will be removed in the left until others a
z = "****//%//Machine learning is fun///***"
print("lstrip(): ", z.lstrip("*/")) 

# rstrip: return stripped (trimmed) string in the right side
# string.rstrip(removed characters)
y = "****////Machine learning is fun///***"
print("rstrip(): ", y.rstrip("*/")) # * or / will be removed in the right (reverse dire
z = "****////Machine learning is fun/%//***"
print("rstrip(): ", z.rstrip("*/")) 

# strip: return stripped (trimmed) string in both sides
# string.strip(removed characters)
y = "****////Machine learning is fun///***"
print("strip(): ", y.strip("*/")) # * or / will be removed in both sides until others a
z = "****////Machine learning is fun/%//***"
print("strip(): ", z.strip("*/")) 

# maketrans: return a translation table to be used in translations
# string.maketrans("original", "changed", "removed")
# translate: return a translated string based on the table from maketrans()
x = "Machine learning is fun!!!"
my_table = x.maketrans("lif", "LIF", "!")
# "l" changes to "L", "i" changes to "I" , "f" changes to "F", "!" is removed.
print("maketrans(): ", my_table)  
# With the unicode, 108 changes to 76, 105 changes to 73, 102 changes to 70, and 33 is 
print("translate(): ", x.translate(my_table))

# partition: return a tuple where the string is parted into three parts
# string.partition("separating string")
x = "Machine learning is fun!!!"
print("partition(): ", x.partition("is"))
# If the separating string appears multiple times, the leftmost one is a separator
y = "Machine is learning is fun!!!"
print("partition(): ", y.partition("is"))

# rpartition: return a tuple where the string is parted into three parts
# string.rpartition("separating string")
x = "Machine learning is fun!!!"
print("rpartition(): ", x.rpartition("is"))
# If the separating string appears multiple times, the rightmost one is a separator
y = "Machine is learning is fun!!!"
print("rpartition(): ", y.rpartition("is"))

# replace: return a string where a specified value is replaced with a specified value
# string.replace("original", "changed", count), where count is optional 
# count is the number of string to be replaced from the left (default is all occurences
x = "Machine learning is fun!!!"
print("replace(): ", x.replace("i", "A")) # all "i" changes to "A"
print("replace(): ", x.replace("i", "A", 1))
print("replace(): ", x.replace("i", "A", 2))

# split: split the string at the specified separator from the left and returns a list
# list = string.split(separted string, the maximum number of split)
# if the separated string appears multiple times, the string separated from the left
x = "Machine learning is fun!!!"
print("split(): ", x.split("is", 1))
y = "Machine is learning is fun!!!"
print("split(): ", y.split("is", 1))
# The default of the maximum number of split is all occurrences.
print("split(): ", y.split("is"))

# rsplit: split the string at the specified separator from the right and returns a list
# list = rstring.split(separted string, the maximum number of split)
# if the separated string appears multiple times, the string separated from the right
x = "Machine learning is fun!!!"
print("rsplit(): ", x.rsplit("is", 1))
y = "Machine is learning is fun!!!"
print("rsplit(): ", y.rsplit("is", 1))
# The default of the maximum number of split is all occurrences.
print("rsplit(): ", y.rsplit("is"))

# splitlines: split a string into a list where each line is a list item
x = "Machine learning\nDeep learning\nFun"
print("A string is with 3 lines below")
print(x)
print("splitlines(): ", x.splitlines()) # each line is an element

# startswith: return true if the string starts with the specified value
x = "Machine learning is fun!!!"
print("startswith(): ", x.startswith("Machine"))
print("startswith(): ", x.startswith("M"))
print("startswith(): ", x.startswith("m"))

# swapcase: swap cases (lowercase to upper case, and uppercase to lowercase)
x = "Machine learning is fun!!!"
print("swapcase(): ", x.swapcase())

# title: convert to the title
# The first character of each word is uppercase, and others are lowercase
x = "Machine learning is fun!!!"
print("title(): ", x.title())
x = "MACHINE learning is fun!!!"
print("title(): ", x.title())

# lower: convert to a string into lowercase
x = "Machine learning is fun!!!"
print("lower(): ", x.lower())

# upper: convert to a string into uppercase
x = "Machine learning is fun!!!"
print("upper(): ", x.upper())

# f-string with print()
# format()
name = "Tom"
gender = "male"
age = 10
text = "Hello {}! Your gender is {}, and your age is {}"
print(text.format(name, gender, age))

# f-string
print("format() method")
print("Hello {}! Your gender is {}, and your age is {}".format(name, gender, age))
print("----------------------------------------------------")
print("f-string")
print(f"Hello {name}! Your gender is {gender}, and your age is {age}")

# f-string with a floating number: {:minimum width.maximum precision f}
# Let's change the minimum width
acc = 100/3
print(f"Accuracy is {acc}%")
print(f"Accuracy is {acc:.3f}%")
print(f"Accuracy is {acc:1.3f}%")
print(f"Accuracy is {acc:2.3f}%")
print(f"Accuracy is {acc:3.3f}%")
print(f"Accuracy is {acc:4.3f}%")
print(f"Accuracy is {acc:5.3f}%")
print(f"Accuracy is {acc:6.3f}%")
print(f"Accuracy is {acc:7.3f}%")
print(f"Accuracy is {acc:8.3f}%")
print(f"Accuracy is {acc:9.3f}%")

# Let's change the maximum precision
acc = 100/3
print(f"Accuracy is {acc}%")
print(f"Accuracy is {acc:.1f}%") 
print(f"Accuracy is {acc:.2f}%")
print(f"Accuracy is {acc:.3f}%")
print(f"Accuracy is {acc:.4f}%")
print(f"Accuracy is {acc:.5f}%")
print(f"Accuracy is {acc:.6f}%")
print(f"Accuracy is {acc:.7f}%")
print(f"Accuracy is {acc:.8f}%")
print(f"Accuracy is {acc:.9f}%")
print(f"Accuracy is {acc:.10f}%")

# maximum precision is required
# minimum width is optional
acc = 92.123456
print(f"Accuracy is {acc}%")
# maximum precision 2
print(f"Accuracy is {acc:.2f}%")
# maximum precision 2 and minimum width 10
print(f"Accuracy is {acc:10.2f}%")
#print(f"Accuracy is {acc:10.f}%") # gives an error