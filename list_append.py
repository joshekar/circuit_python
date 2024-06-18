# LISTS - Append, Extend, Concatenate
print('''LISTS - Assigning values by using Append, Extend, Concatenate
Learn more about Lists here:
https://www.w3schools.com/python/python_lists.asp
''')      
print('''
Challenge #1 Fibonacci
Run, then Edit the code in the template example:
      
fibonacci_sequence = [0,1,1,2,3, 5, 8, 13, 21, 34]
Rather than just creating the list with the number, 
write a program to calculate the fibonacci number and then 
append, extend and concatenate the sequence
- See how the append works with fibonacci_sequence[0]+
  fibonacci_sequence[1]
- Do this again to append the next value in the sequence.

      ''')
fibonacci_sequence = [0,1]
print(fibonacci_sequence)
# .append method to Appending to the list
fibonacci_sequence.append(fibonacci_sequence[0]+fibonacci_sequence[1])
print(fibonacci_sequence)
# Use the .append to add the next number in the sequence.
fibonacci_sequence.append(fibonacci_sequence[1]+fibonacci_sequence[2])
print(fibonacci_sequence)

fibonacci_sequence.append(fibonacci_sequence[2]+fibonacci_sequence[3])
print(fibonacci_sequence)

x=fibonacci_sequence[3]+fibonacci_sequence[4]
fibonacci_sequence.append(x)
print(fibonacci_sequence)

fibonacci_sequence.append(fibonacci_sequence[4]+fibonacci_sequence[5])
print(fibonacci_sequence)

fibonacci_sequence.append(fibonacci_sequence[5]+fibonacci_sequence[6])
print(fibonacci_sequence)

fibonacci_sequence.append(fibonacci_sequence[6]+fibonacci_sequence[7])
print(fibonacci_sequence)

fibonacci_sequence.append(fibonacci_sequence[7]+fibonacci_sequence[8])
print(fibonacci_sequence)
