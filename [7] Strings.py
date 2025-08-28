# PRINT A STRING

a = "Hello"
print(a)

# STRINGS ARE ARRAYS

a = "Hello world"
print(a[0])

# LOOPING THROUGH A STRING

for i in "banana":
    print(i)

# STRING LENGTH

a = "Hello World"
print(len(a))

# CHECKING A STRING

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "free" not in txt:
   print("No, free is not present.")

# SLICING A STRING

a = "Hello, World!"
print(a[2:4]) # This will print characters from index 2 to 4 (not including 4)

# -----------------------------------------------

a = "Hello, World!"
print(a[:4])

# -----------------------------------------------

a = "Hello, World!"
print(a[2:])

# -----------------------------------------------

a = "Hello, World!"
print(a[-5:-2])

# MODIFYING A STRING

a = "Hello, World!"
print(a.upper()) # This will convert the string to upper case

# -----------------------------------------------

a = "Hello, World!"
print(a.lower()) # This will convert the string to lower case

# -----------------------------------------------

a = " Hello, World! "
print(a.strip()) # This will remove any whitespace from the beginning or the end

# -----------------------------------------------

a = "Hello, World!"
print(a.replace("H", "J")) # This will replace H with J

# -----------------------------------------------

a = "Hello, World!"
print(a.split(",")) # This will split the string into a list where there is a comma

# STRING CONCATENATION

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# STRING FORMAT

age = 16
txt = f"My name is Mridul, and I am {age}"
print(txt)

# ------------------------------------------------

price = 50
txt = f"The price of chips is {price:.2f} rupees" # This will format the price to 2 decimal places
print(txt) 

# -------------------------------------------------

txt = f"The price is {20 * 59} dollars"
print(txt)

# ESCAPE CHARACTER

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hi \n Mridul"
print(txt)