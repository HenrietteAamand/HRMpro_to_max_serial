from json import JSONEncoder
import json

class Max_dataobj_class():
    def __init__(self) -> None:
        pass
    def UpdateJSON(self, hr, timestamp):
        self.timestamp = timestamp
        self.hr = hr

    def Get_Empty_JSON(self):
        self.timestamp = 0
        self.hr = 0
        theObjectAs_PyObj = json.loads(self.toJSON())
        return theObjectAs_PyObj

    def toJSON(self): #Denne metode bruges til at serialisere ppg objektet. Den returnere et json objekt. 
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)