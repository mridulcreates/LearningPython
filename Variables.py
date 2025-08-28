#  VARIABLES

x =  7 # integer variable
y = "Mridul" # string variable

print(x) 
print(y)

# ------------------------------------------------- 

x = str(3)   # x will be '3'
x = float(3) # x will be 3.0
x = int(3) # x will be 3

# ------------------------------------------------- 

x = 7
y = "Mridul"

print(type(x))
print(type(y))

# VARIABLE NAMES

myVariableName = "Mridul" # Camel Case
MyVariableName = "Mridul" # Pascal Case
my_variable_name = "Mridul" # Snake Case

# MULTIPLE VALUE ASSIGNMENT VARIABLES

x, y, z = "Mridul", "Arnav", "Ritvik"
print(x)
print(y)
print(z)
print(x, y, z)

x = y = z = "Mridul"
print(x, y, z)

agents = ["neon", "reyna", "jett"]
x, y, z = agents
print(x , y, z)

x = "Python "
y = "is "
z = "trash "
print(x + y + z)

x = 5
y = 10
print(x + y)
print(x, y)

# GLOBAL VARIABLES

x = "mridul"

def myFunc():
    print("he is " + x)

myFunc()
print(x)


x = "mridul"

def myfunc():
    x = "ritvik"
    print(x)

myfunc()
print(x)


x = "mridul"
def myFunc():
    global x
    x = "ritvik"

myFunc()

print("Python is " + x)