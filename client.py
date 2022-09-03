class Client:
    name =""
    age = 0
    id = ""


    def __init__(self, name="", age=0, id=""):
        self.name = name
        self.age = age
        self.id = id
        pass
        
    def __str__(self):
        return f'"Name":{self.name}, "Age":{self.age}, "ID":{self.id}'
    