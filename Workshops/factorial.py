"""
@author: emretosun

"""
num = int(input("Value =? "));
till = 1;
result = 1;
if num < 0:
    result = "Can't have negative factorial!";
else:
    while num > till:
        result *= num;
        num -= 1;
print("Result is: " + str(result));