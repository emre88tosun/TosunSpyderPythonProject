"""
@author: emretosun

"""
import os;
students = ["John", "Jane", "Mike", "Anderson", "Jenny"];
os.chdir("../Workshops");
appendingFile = open("students.txt","a");
for index, student in enumerate(students):
    appendingFile.write(student);
    if index != len(students)-1:
        appendingFile.write("\n");
appendingFile.close();