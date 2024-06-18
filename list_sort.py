print('''LISTS - Methods - sort(), pop(), del, remove()
Learn more about Lists here:
https://www.w3schools.com/python/python_lists.asp
''')      
print('''
Challenge #1 
Run, then Edit the code in the template example:

On the following lists, use the sort(), pop(), del, remove() methods
      ''')
# sort()
my_list = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d",]
print(my_list)
# use sort()
my_list.sort()
print(my_list)

# pop()
my_list = ["STEAM", "Clown", "Productions"]
print(my_list)
# use pop()
x=my_list.pop(0)
print(my_list)

# del
my_list = ["apple", "orange", "pomegranate", "pineapple"]
print(my_list)
# use del
del my_list[2]
print(my_list)

# remove() "Shadow"
my_list = ["Centauri", "Minbari", "Narn", "Human", "Shadow", "Vorlon"]
print(my_list)
# use remove()
my_list.remove("Shadow")
print(my_list)

