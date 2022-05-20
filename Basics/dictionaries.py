"""
@author: emretosun

"""
emptyDictionary = {};
# print(emptyDictionary);
intKeyDictionary = { 1: "Emre", 2: "Tosun", 3: 16 };
# print(intKeyDictionary);
mixedKeyDictionary=  { "name": "Emre", 1: [2, 4, 6] };
# print(mixedKeyDictionary);
myDict = dict({ 1: "apple", 2: "pencil" });
# print(myDict);
mySecondDict = dict([ (1,"car"), ("name","Tesla") ]);
# print(mySecondDict);
dictionary = {
    "book": "kitap",
    "car": "araba",
    "pencil": "kurşun kalem",
    "ball": "top"
    };
# print(dictionary);
# print(dictionary["car"]);
# dictionary["pencil"] = "kalem";
dictionary["table"] = "masa";
# print(dictionary);
secondDictionary = dict({
    "window": "pencere",
    "door": "kapı"
    });
# print(secondDictionary);
thirdDictionary = dict(eraser = "silgi", chalk = "tebeşir");
del(thirdDictionary["eraser"]);
# print(thirdDictionary);
# print(len(thirdDictionary));