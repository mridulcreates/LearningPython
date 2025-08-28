# TYPES OF NUMBERS AND THEIR TYPES

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

# CONVERTING TYPES OF VARIABLES

a = float(x)
print(a) # This will convert x (int) to (float).. i.e -> 1 to 1.0

# RANDOM NUMBER

import random
print(random.randrange(1, 10))
print(random.randrange(0, 10, 2)) # This will print even numbers between 0 to 10

colors = ["red", "blue", "green"]
print(random.choice(colors))
print(random.choice(colors, 2)) # This will print 2 random colors from the list

