# if your want moke the the database we create a python class object here 
# we can fake the models by simpley writing python calls 
# useing this we can change our serializers to models serializers and use Person
#object as models object.it's not a persistent data

class Person(object):
    def __init__(self, username, firstname,lastname):
        self.username = username
        self.firstname = firstname
        self.firstname = lastname
