# this is an example of try/escept
print('This is a Guessing Game')
print("Ready to play?")

print("Input the user number:")
user_guess = input()
try:
    user_guess = int(user_guess)

except:
    print('Please enter a number')
    print(user_guess, 'is NOT a number')
    
