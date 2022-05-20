"""
@author: emretosun

"""
numbers = [1, 2, 3, 4, 5];
# squares = [];
# for number in numbers:
#     squares.append(number*number);
squares = list(map(lambda x: x**2, numbers));
print(squares);
cubes = list(map(lambda x: x**3,numbers));
print(cubes);