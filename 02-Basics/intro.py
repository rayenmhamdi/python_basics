#Variables : https://www.w3schools.com/python/python_variables.asp
#Conditional Structure : https://www.w3schools.com/python/python_conditions.asp
# Iterative Structure : 

# This is a comment
"""
This is
a multiline comment
"""


# Declare/Init variables
a = 5
b = "c"
c = 'd'
d = "Hello World"
e = 14.9
f = 25598745255696.500
g = True
h = False
i, j = 5 , "MJO"
k, l , m = "Hello", "Maroua", 'Jomaa'
n = 5
n = n + 1
n += 1
n -= 1
n *= 5
n /= 5


# variable types
res = type(a)
res = type(b)
res = type(c)
res = type(d)
res = type(e)
res = type(f)
res = type(g)
res = type(h)

# variable casting : str() - int() - float() - bool()
res = str(a)
res = str(f)
res = int("2022")
res = float("15.6")
res = bool("1")
res = bool("True")


# Input/Output
print(k)
print(k, l, m)
print("K value = ", k)
print("i value = ", str(i))
message = "i value = " + str(i)
print(message)
print("This is a new line message", end=" ")
print("This line will be printed with the above")

age = input()
age = input("enter your age 1 : ")
print(type(age))

age = float(input("enter your age 2 : "))
print(type(age))

age = input("enter your age 3 : ")
age = float(age)
print(type(age))




# Conditional Structure
a = 33
b = 200
if b > a:
    print("b is greater than a")


if a > b: print("a is greater than b")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


a = 2
b = 330
print("A") if a > b else print("B")

res = a if a > b else b

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")





# While / For
i = 1
while i < 6:
    print(i)
    i += 1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


for x in "banana":
    print(x)



for x in range(20):
    print(x)

for x in range(5,20):
    print(x)

for x in range(5,20,2):
    print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)



