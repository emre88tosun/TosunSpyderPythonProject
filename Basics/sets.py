"""
@author: emretosun

"""
emptySet = {};
# print(emptySet);
intSet = { 1, 2, 4 };
# print(intSet);
stringSet = set({"Istanbul","Ankara","Izmir"});
print(stringSet);
mixedSet = { 4, "Emre", 3.14, (1, 2, 3) };
# print(mixedSet);
duplicateSet = { 1, 2, 3, 3 };
# print(duplicateSet);    #OUTPUT: {1, 2, 3}
studentsSet = { "Emre", "Ayşe", "Deniz", "Ali" };
# for student in studentsSet:
#     print(student);
# print("Emre" in studentsSet);
# if "Emre" in studentsSet:
#     print("Voila!");
# else:
#     print("Nay!");
studentsSet.add("Veli");
studentsSet.update(["Merve","Mert"]);
# print(studentsSet);
# print(len(studentsSet));
# studentsSet.remove("veli");
# studentsSet.remove("Veli");
# studentsSet.discard("Veli");
# subSet = studentsSet.pop();
# cleanSet = studentsSet.clear();
# del studentsSet;
print(studentsSet);