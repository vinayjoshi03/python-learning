import json
class Vehicle:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    @classmethod
    def modifyColor(cls, newType, newColor):
        #print("color: ", newColor)
        return cls(newType,newColor)


vehicleObject = Vehicle("Two", "Blue");
print(vehicleObject.color, "--",vehicleObject.type)
returnValue = vehicleObject.modifyColor('Four', 'Red')
print(returnValue.color, "--",returnValue.type)
#print(vehicleObject.type, vehicleObject.color)

class GetData:
    jsonDataDump = {
        "name":'vinay',
        "data":[{
            "username":'vinayjoshi'
        }]
    }

    listDataDump = [10,20,30,40]


    def getName(self):
        return self.jsonDataDump.values()



objnew = GetData();
print(objnew.getName());




