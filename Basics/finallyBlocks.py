"""
@author: emretosun

"""
import sys;
list = [7, "emre", 0, 3, "6"];
for value in list:
    try:
        print("Value is:", str(value));
        result = 1 / (int(value));
        print("Result is:",result);
    except ValueError:
        print(value + " is not an integer.");
    except ZeroDivisionError:
        print("Dividing number can't be zero.");
    except:
        print("An error occurred!", sys.exc_info()[0]);
    finally:
        print("Operation is done for " + str(value) + ".");