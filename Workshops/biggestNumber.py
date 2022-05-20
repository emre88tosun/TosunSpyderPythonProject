"""
@author: emretosun

"""
firstInput = int(input("First number =? "));
secondInput = int(input("Second number =? "));
thirdInput = int(input("Third number =? "));
if firstInput >= secondInput and firstInput >= thirdInput:
    print(str(firstInput) + " is the greatest.");
elif secondInput >= firstInput and secondInput >= thirdInput:
    print(str(secondInput) + " is the greatest." );
else:
    print(str(thirdInput) + " is the greatest.");