class Message:
 def __init__(self,sender,receiver, recipients,message):
   self.sender = sender
   self.receiver = receiver
   self.recipients = recipients
   self.message = message

class Character:
 def __init__(self, name):
  self.name = name
  self.loggedOn = False
  self.npc = False
  self.description =""
  self.location = "Start"
  self.inventory = []
  self.level = 1
  self.password = ""
  self.log = []

class Object:
 def __init__(self,name):
  self.name = name
  self.description = False
  self.taken = False
  self.location = 0
  self.owner = 0
  self.state ="normal"

class World:
 def __init__(self,name):
  self.name = name
  self.characters = []
  self.objects = []
  self.switches = {}
  self.worldmap = []
 def getLoggedOn(self):
  aux = []
  for car in self.characters:
    if car.loggedOn ==True:
     aux.append(car.name)
  return aux

 def getCharacterByName(self,name):
  for car in self.characters:
   if car.name == name:
    return car
  return False


 def getObjectByName(self,name):
  for car in self.objects:
   if car.name == name:
     return car
   return False


 def addCharacter(self,char):
  self.characters.append(char)
  return
 
 def getObjectsByLocation(self,location):
  aux = []
  for obj in self.objects:
   if obj.location == location:
    aux.append(obj)
  return aux

 def getCharactersByLocation(self,location):
  aux = []
  for car in self.characters:
    if car.location == location and car.loggedOn==True:
     aux.append(car)
  return aux
 
 def getMapElementByName(self,name):
  for el in self.worldmap:
    if el.name == name:
     return el
  return False

 def move(self, charname,direct):
  car = self.getCharacterByName(charname)
  pos = self.getMapElementByName(car.location)
  newposname = pos.go[direct]
  if pos.go[direct]!="":
    car.location= self.getMapElementByName(newposname).name
    return newposname
  else:
    return ""

 def take(self,charname,objname):
   car = self.getCharacterByName(charname)
   obj = self.getObjectByName(objname)
   if car.location == obj.location:
    obj.taken = True
    obj.location = 0 
    car.inventory.append(obj.name)
    return True
   else:
    return False

 def drop(self,charname,objname):
   car = self.getCharacterByName(charname)
   obj = self.getObjectByName(objname)
   if objname in car.inventory:
    obj.taken = False
    obj.location = car.location
    car.inventory.remove(objname)
    return True
   else:
    return False



class MapElement:
 def __init__(self,name):
  self.name = name
  self.go ={}
  self.description = ""
  self.go["north"] = ""
  self.go["south"] = ""
  self.go["west"] = ""
  self.go["east"] = ""
  self.switches =""
  self.onGo = ""

    
