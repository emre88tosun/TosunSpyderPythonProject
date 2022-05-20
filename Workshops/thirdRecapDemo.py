"""
@author: emretosun

"""
userInput = int(input("Number =? "));
isPrime = True;
for value in range(2,userInput):
    if userInput%value == 0:
        isPrime = False;
        break;
if isPrime:
    print(str(userInput) + " is a prime number.");
else:
    print(str(userInput) + " isn't a prime number.");