"""
@author: emretosun

"""
# num = 3.14;
# if num > 0:
#     print("Positive number");
# elif num == 0:
#     print("Zero");
# else:
#     print("Negative number");
# inputNum = int(input("Value =? "));
# if inputNum > 0:
#     print(str(inputNum) + " is positive");
# elif inputNum == 0:
#     print("0 is zero");
# else:
#     print(str(inputNum) + " is negative");
firstNum = 10;
secondNum = 20;
if firstNum > secondNum:
    print(str(firstNum) + " is greater than " + str(secondNum));
elif firstNum == secondNum:
    print(str(firstNum) + " is equals to " + str(secondNum));
else:
    print(str(firstNum) + " is less than " + str(secondNum));
thirdNum = int(input("Third num =? "));
fourthNum = int(input("Fourth num =? "));
if thirdNum > fourthNum:
    print(str(thirdNum) + " is greater than " + str(fourthNum));
elif thirdNum == fourthNum:
    print(str(thirdNum) + " is equals to " + str(fourthNum));
else:
    print(str(thirdNum) + " is less than " + str(fourthNum));