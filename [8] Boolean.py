# BOOLEANS 

print(10 < 9) # This will return False because 10 is not less than 9

# -----------------------------------------------

print(bool("Hello")) 
print(bool(7))

# -----------------------------------------------

def myfunc():
    return False

print(bool(myfunc()))

# -----------------------------------------------

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")