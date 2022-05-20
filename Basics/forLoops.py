"""
@author: emretosun

"""
# numbers = [1, 3, 4, 6, 9,12];
# sum = 0;
# for value in numbers:
#     sum += value;
# print("The sum is:",sum);
cities = ["Istanbul", "Ankara", "Izmir", "Bursa"];
# for city in cities:
#     # print("City code is:",city[0:3]);
#     if city == "Ankara":
#         print("Angara!");
#     else:
#         print(city);
for city in cities:
    if city == "Ankara":
        break;
    else:
        print("City is:",city);
    #OUTPUT: City is: Istanbul
for city in cities:
    if city == "Ankara":
        continue;
    else:
        print("City is:",city);
    #OUTPUT: City is: Istanbul
    #OUTPUT: City is: Izmir
    #OUTPUT: City is: Bursa
