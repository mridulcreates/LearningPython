# PYTHON LISTS

mylist = ["mridul", "ritvik", "arnav"]
print(mylist)
print(len(mylist))
print(type(mylist))

# ------------------------------------------------

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# ------------------------------------------------

list1 = ["Mridul", 16, True, "male"]

# LIST CONSTRUCTOR

mylist = list(("mridul", "ritvik", "arnav"))
print(mylist)

# ACCESSING LIST ITEMS

thislist = ["apple", "banana", "cherry", "mango", "watermelon"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:4])
print(thislist[:5])
print(thislist[2:])
print(thislist[-2:-5])

# -------------------------------------------------

thislist = ["apple", "banana", "cherry", "mango", "watermelon"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")