"""
@author: emretosun

"""
class Math:
    def __init__(self, num1, num2):
        self.num1 = num1;
        self.num2 = num2;
    def add(self):
        return self.num1 + self.num2;
    def sub(self):
        return self.num1 - self.num2;
    def multiply(self):
        return self.num1 * self.num2;
    def divide(self):
        return self.num1 / self.num2;
firstMath = Math(2, 86);
secondMath = Math(101, 7);
# print("Add:",firstMath.add());
# print("Sub:",secondMath.sub());
# print("Multiply:",firstMath.multiply());
# print("Divide:",secondMath.divide());