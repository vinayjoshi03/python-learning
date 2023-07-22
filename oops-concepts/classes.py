import json


class Vehicle:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    @classmethod
    def modifyColor(cls, newType, newColor):
        # print("color: ", newColor)
        return cls(newType, newColor)


vehicleObject = Vehicle("Two", "Blue");
print(vehicleObject.color, "--", vehicleObject.type)
returnValue = vehicleObject.modifyColor('Four', 'Red')
print(returnValue.color, "--", returnValue.type)


# print(vehicleObject.type, vehicleObject.color)

class GetData:
    aList = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4},[{
        "data": [
            {"name":"Vinay"},
            {"name": "Joshi"}
        ]
    }]]



    def getName(self):
        print(type(self.aList))
        jsonString = json.dumps(self.aList)
        print("jsonString-->", type(jsonString));
        return jsonString;


objnew = GetData();
jsonListData = json.loads(objnew.getName())
print(jsonListData[0]['b'])

'''
Running for loop on list
'''

for x in jsonListData:
    print(x)


def print1():
    print("Printing string 1")

def print2():
    print("Printing string 2")


printSwitcher = {
    "print1": print1,
    2: print2
}


def printData(param):
    printSwitcher.get(param)()

printData(2)
printData("print1")