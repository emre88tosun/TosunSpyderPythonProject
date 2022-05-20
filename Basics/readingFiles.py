"""
@author: emretosun

"""
# r = Read, a = Append, w = Write, x = Create
file = open("customers.txt","r");
# print(file.read());
# print("*******");
# print(file.readline());
# print(file.readline());
# for line in file:
#     print(line);
file.close();
# appendingFile = open("students.txt","a");
# appendingFile.write("\n");
# appendingFile.write("John");
# appendingFile.write("\n");
# appendingFile.write("Jane");
# appendingFile.close();
import os;
if os.path.exists("students.txt"):
    print("Exists!");
else:
    print("Doesn't exist!");
# os.remove("students.txt");
# os.rmdir("empty");
# os.mkdir("empty")