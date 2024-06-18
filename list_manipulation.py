# LISTS - Assigning values by indexing them
print('''LISTS - Assigning values by indexing them
Learn more about Lists here:
https://www.w3schools.com/python/python_lists.asp
''')      
print('''
Challenge #1
Run, then Edit the code in the template example:
      
The goal is to update the values of my_list to be 
in nummerical order 1,2,3,4,5,6,7,8,9 by directly 
assigning the values
- Fix the value at my_list[0] by re-assigning it with 1
- Fix the value at index 2 by re-assigning it with the 
  appropriate value
- Fix the value at index 5 thru 6 by re- 
  assigning it with the list values [n,n+1]
- Fix the value at index -1 by re-assigning it with the 
  appropriate value
      ''')
my_list = [8,2,6,4,5,7,1,8,3]
print(my_list)
# fixing index 0
my_list[0] = 1
print(my_list)
# fixing index 2
my_list[2] = 3
print(my_list)
# fixing index 5 thru 6 (up to 7)
my_list[5:7] = [6,7]
print(my_list)
# fixing index -1
my_list[-1] = 9
print(my_list)
