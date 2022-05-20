"""
@author: emretosun

"""
def sayHello():
    print("Hello stranger!");
def greetings(name = "my friend"):
    print("Hello, " + name + "! Have a nice day.");
def greetWithFullname(name = "john", surname = "doe"):
    print("Hello, " + name + " " + surname +"." );
def returnName(name):
    return name.upper();
returnUpperName = lambda name: name.upper();
print(returnUpperName("aliveli"));
print(type(returnUpperName));
x = returnUpperName;
