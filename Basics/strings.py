"""
@author: emretosun

"""
firstString = "FirST StRIng!";
secondString = "fIRsT sTRiNg!";
if firstString.upper() == secondString.upper():
    print("The string are same!");
else:
    print("The strings are not same!");
thirdString = "HelLo WOrlD";
# print(thirdString[3:5]);
# print(thirdString[2:]);
# print(thirdString[:4]);
# print(len(thirdString));
# print(thirdString[len(thirdString)-1]);
lowerString = thirdString.lower();
upperString = thirdString.upper();
# print(lowerString + " " + upperString);
replacedString = thirdString.replace("e","i");
# print(replacedString);
myInfo = "  Emre Tosun 88 Ankara  ".strip();
# print(myInfo.split(" "));
secondInfo = "Emre_Tosun_06_Inegol";
# print("Name: " + secondInfo.split("_")[0]);
# name = input("Your name? ");
# firstInt = input("First int =? ");
# secondInt = input("Second int =? ");
# print(name.upper() + ": " + str(int(firstInt)+int(secondInt)))