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


# CHANGE LIST ITEMS

thislist = ["mridul", "ritvik", "arnav"]
thislist[1] = "sahil"
print(thislist)

thislist[1:3] = ["harman", "sarthak"] # Replaces items from index 1 to 3 (not including 3)
print(thislist)

# INSERTING ITEMS

thislist = ["mridul", "ritvik", "arnav"]
thislist.insert(2, "sahil") # Inserts any value to a particular index
print(thislist)

# ADD LIST ITEMS

thislist = ["mridul", "ritvik", "arnav"]
thislist.append("sahil") # Adds an item to the end of the list
print(thislist)

# EXTEND A LIST

thislist = ["mridul", "ritvik", "arnav"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)

# ADD ANY ITERABLE

thislist = ["apple", "banana", "cherry"]
thislist2 = [[1, 2, 3], [4, 5, 6]]
thislist.extend(thislist2)
print(thislist)

# REMOVE LIST ITEMS

thislist = ["mridul", "ritvik", "arnav"]
thislist.remove("ritvik") # Removes a specified item
print(thislist)

# -------------------------------------------------

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # Only the first occurrence of banana will be removed

# -------------------------------------------------

thislist = ["mridul", "ritvik", "arnav"]
thislist.pop(0)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# -------------------------------------------------

thislist = ["mridul", "ritvik", "arnav"]
del thislist[0]
print(thislist)

thislist.clear()
print(thislist) # Empties the list

# LOOPING THROUGH A LIST

thislist = ["mridul", "ritvik", "arnav"]
for i in thislist:
    print(i)

thislist = ["mridul", "ritvik", "arnav"]
# len(thislist) = 3 → range(3) = [0,1,2]
# loop runs with i = 0,1,2 → prints thislist[i]
for i in range(len(thislist)):
    print(thislist[i])

# USING WHILE LOOP

thislist = ["mridul", "ritvik", "arnav"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# LIST COMPREHENSION

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist) # prints all elements except apple

newlist = [x for x in range(10) if x < 5] # accept numbers only < 5

# SORT LISTS

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #  sort the list alphanumerically, ascending, by default

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# ---------------------------------------------

def myfunc(n):
  return abs(n - 50) # returns distance of n from 50

thislist = [100, 50, 65, 82, 23]
# sort() uses myfunc → elements are ordered by closeness to 50
thislist.sort(key = myfunc)
print(thislist) # Sort the list based on how close the number is to 50

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# COPY LISTS

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# JOIN LISTS

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)