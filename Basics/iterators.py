"""
@author: emretosun

"""
import sys;
cities = ["Istanbul", "Ankara", "Izmir"];
firstIterator = iter(cities);
# try:
#     print(next(firstIterator));
#     print(next(firstIterator));
#     print(next(firstIterator));
#     print(next(firstIterator));
# except StopIteration:
#     print("Error: Out of range.");
# except:
#     print("An error occurred:",sys.exc_info());
for city in cities:
    print("City is:",city);