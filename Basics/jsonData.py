"""
@author: emretosun

"""
import json;
data = '{"firstName": "Emre", "lastName": "Tosun"}';
jData = json.loads(data);
# print(jData["firstName"] + " " + jData["lastName"]);
customer = {
        "firstName": "Jane",
        "lastName": "Doe",
        "username": "doe_jane",
    };
customerJson = json.dumps(customer);
# print(customerJson);
# print(type(json.dumps(["emre","tosun"])));