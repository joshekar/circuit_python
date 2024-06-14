# this is my number guessing program
print('This is a Guessing Game')
print("Ready to play?")

# Add more code here
# 1) use an IF statement to check if 
#    number_2_guess = user_guess
# 2) print if they are
# 3) use ELSE to print if they are not

# Run the program with user_guess = 5 and then edit 
# the source code to change it to user_guess = 7

print("Input the user number:")
user_guess = input()
number_2_guess = 4

if (number_2_guess == int(user_guess)):
    print ("They are the same")
else:
    print("They are not the same")
