"""
@author: emretosun

"""
try:
    value = int(input("Enter an integer =? "));
    value2 = int(input("Enter the second integer =?"));
    print("Result is: ", value/value2);
except ValueError:
    print("Do not enter non numeric input.");
except ZeroDivisionError:
    print("Dividing number can not be zero.");
except:
    print("An error occurred.");