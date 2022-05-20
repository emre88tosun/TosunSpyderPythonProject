"""
@author: emretosun

"""
emptyArray = [];
intArray = [1, 2, 3, 4, 5];
mixedArray = ["Emre", "Tosun", 88, 3.14];
nestedArray = ["py", [5, 12, 13], 6.8];
studentArray = ["Ali", "Ayşe", "Fatma"];
# print(studentArray[1]);
studentArray.append("Deniz");
studentArray.remove("Ayşe");
studentArray[1] = "Veli";
# print(studentArray);
# for value in studentArray:
#     print(value);
citiesArray = list(("Istanbul","Ankara","Istanbul"));
# print(citiesArray);
# print(len(citiesArray));
# print(citiesArray.clear());
print("Istanbul count is: " + str(citiesArray.count("Istanbul")));
print("Index of Ankara is: " + str(citiesArray.index("Ankara")));
citiesArray.pop(1);
citiesArray.insert(0,"Izmir");
citiesArray.reverse();
# print(citiesArray);
citiesArray1 = citiesArray.copy();
citiesArray2 = citiesArray;
citiesArray2[0] = "Ankara";
# print(citiesArray);
# print(citiesArray1);
citiesArray.extend(citiesArray1);
citiesArray.sort();
citiesArray.reverse();
print(citiesArray);