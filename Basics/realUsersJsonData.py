"""
@author: emretosun

"""
import json;
import os;
os.chdir("../Basics");
with open("users.json") as users:
    usersData = json.load(users);
    for x in range(5):
        print(usersData[x]["name"]);
        print(usersData[x]["email"]);
        print(usersData[x]["address"]["street"]);
        print(usersData[x]["address"]["geo"]);
        print(usersData[x]["address"]["geo"]["lat"]);
    