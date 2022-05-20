"""
@author: emretosun

"""
from Modules.mathModule import *;
print("Choose action:\n[1] Add numbers\n[2] Sub numbers\n[3] Multiply numbers\n[4] Divide numbers");
selection = int(input(""));
num1 = int(input("First number =? "));
num2 = int(input("Second number =? "));
if selection == 1:
    mathModule.add(num1,num2);
elif selection == 2:
    mathModule.sub(num1,num2);
elif selection == 3:
    mathModule.multiply(num1,num2);
elif selection == 4:
    mathModule.divide(num1,num2);
else:
    print("Unknown action. Please try again.");