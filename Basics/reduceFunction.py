"""
@author: emretosun

"""
from functools import reduce;
numbers = [1, 2, 3, 4, 5];
factorials = reduce(lambda x,y: x*y, numbers);
print(factorials);