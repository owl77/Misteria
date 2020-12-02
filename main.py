import classes
import world
import pickle
import signal
import sys
import os
import parser
import time

def getpids():
 f = open('pids','rb')
 pids = pickle.load(f)
 f.close()
 return pids

def register():
 mypid = os.getpid()
 f = open('pids','rb')
 pids = pickle.load(f)
 f.close()
 pids.append(mypid)
 f = open('pids','wb')
 pickle.dump(pids,f)
 f.close()

def deregister():
 mypid = os.getpid()
 f = open('pids','rb')
 pids = pickle.load(f)
 f.close()
 pids.remove(mypid)
 f = open('pids','wb')
 pickle.dump(pids,f)
 f.close()

def findnew(newlist,oldlist):
 aux = []
 for x in newlist:
  if not x in oldlist:
   aux.append(x)
 return aux

def findgone(newlist,oldlist):
 aux = []
 for x in oldlist:
  if not x in newlist:
    aux.append(x)
 return aux

def sighandler(signum,stack):
 passupdate()
 return 

def messhandler(signum,stack):
 file = open('messages','rb')
 mess = pickle.load(file)
 file.close()
 if mycharacter.name in mess.recipients:
  if mess.receiver == mycharacter.name:
   print(mess.sender+" tells you: "+mess.message)
  else:
    print(mess.sender+" to "+ mess.receiver+": "+mess.message)


def change(oldobjs,oldcars):
 objs = [o.name for o in Misteria.getObjectsByLocation(mycharacter.location)]
 cars = [o.name for o in Misteria.getCharactersByLocation(mycharacter.location)]
 newobjs= findnew(objs,oldobjs)
 newcars = findnew(cars,oldcars)
 goneobjs = findgone(objs,oldobjs)
 gonecars = findgone(cars,oldcars)
 for x in newobjs:
  print(x +" appears.")
 for x in newcars:
  print(x +" entered.")
 for x in goneobjs:
  print(x +" is gone.")
 for x in gonecars:
  print(x + " has left.")
 return

signal.signal(signal.SIGUSR1,sighandler)
signal.signal(signal.SIGUSR2,messhandler)

def universalsig():
 pids = getpids()
 if len(pids) >0:
  for p in pids:
   if p!=os.getpid():
    os.kill(p,signal.SIGUSR1)

def messsig():
 pids = getpids()
 if len(pids) >0:
  for p in pids:
   if p!=os.getpid():
    os.kill(p,signal.SIGUSR2)


print("(C)reate new character")
print("(L)ogin")
print("(E)xit")
print("")

def actupdate(world):
 f = open('world','wb')
 pickle.dump(world,f)
 f.close()


def passupdate():
 global Misteria
 oldobjs = [o.name for o in Misteria.getObjectsByLocation(mycharacter.location)]
 oldcars = [o.name for o in Misteria.getCharactersByLocation(mycharacter.location)]
 f = open('world','rb')
 Misteria = pickle.load(f)
 f.close()
 change(oldobjs,oldcars)
 return

f = open('world','rb')
Misteria = pickle.load(f)
f.close()
me =""

  
def createcharacter():
 nam = input("Name of Character: ")
 if Misteria.getCharacterByName(nam)!=False:
  print ("Name already taken.")
  return
 desc = input("Brief description of Character: ")
 mycharacter = classes.Character(nam)
 mycharacter.description = desc
 ps = True;
 while(ps):
  psw = input("Choose password: ")
  psw2 = input("Confirm password: ")
  if psw2 == psw:
   mycharacter.password = psw
   ps = False
  else:
   print("Passwords did not match.")
 print("")
 print("Character successfully created.")
 print("")
 Misteria.addCharacter(mycharacter)
 actupdate(Misteria)
 universalsig()
 return
 
def look(l):
 print("")
 print("")
 print("")  
 print(" *==*==*==* "+l+ " *==*==*==*")
 print("")
 print("")
 print("")
 loc = Misteria.getMapElementByName(l)
 print(loc.description)
 print("")
 print("")
 print("")
 print("")
 print("")
 print("")
 objs = Misteria.getObjectsByLocation(l)
 if len(objs)>0:
  print("You see:")
  print("")
  for o in objs:
   print(o.name)
  print("")
 cars = Misteria.getCharactersByLocation(l)
 if len(cars)>0:
  for o in cars:
   if o.name!= mycharacter.name and o.loggedOn==True:
    print(o.name)
  print("")
 return

def mainloop():
 name = mycharacter.name
 while(True):
  inp = input(name + "> ")
  pinp = parser.preparse(inp)
   
  mylocation = Misteria.getCharacterByName(name).location
  myobjects = Misteria.getObjectsByLocation(mylocation)
  myobjectnames = [o.name for o in myobjects]
  mycharacters = Misteria.getCharactersByLocation(mylocation)
  mycharacternames = [o.name for o in mycharacters]
  if inp=="Items":
   print(" ======= Items ======== ")
   for o in Misteria.getCharacterByName(name).inventory:
    desc = Misteria.getObjectByName(o).description
    print(o+": " + desc)
  if inp=="H":
   print("")
   print("Implemented Commands:")
   print("")
   print("Look : examine surroundings")
   print("Examine <being> : examine person or object")
   print("Take <object>")
   print("Drop <object>")
   print("Items : list inventory")
   print("Who : list of active users")
   print("Tell <recipient> <message> : send message to someone. Can be heard by everyone in the room.")
   print("N,S,W,E: go North, South, West, East")
   print("Quit")
   print("")
  if inp=="Quit":
   print("Goodbye " + name +"!")
   Misteria.getCharacterByName(name).loggedOn =False
   actupdate(Misteria)
   universalsig()
   deregister()
   return
  
  if inp=="Who":
   for x in [c.name for c in Misteria.characters if c.npc ==False and c.loggedOn ==True]:
    print(x)

  if inp=="Look":
    look(Misteria.getCharacterByName(name).location)

  if pinp.verb=="Examine":
  
   if  pinp.directobject in myobjectnames:
    print(Misteria.getObjectByName(pinp.directobject).description)
   else:
    if not pinp.directobject in mycharacternames:
     print("There is no "+pinp.directobject +" here.")
 
   if pinp.directobject in mycharacternames:
    print(Misteria.getCharacterByName(pinp.directobject).description)
   else: 
    if pinp.directobject in [c.name for c in Misteria.characters]:
     print(pinp.directobject +" is not here.")
 

  if pinp.verb=="Tell":
   if pinp.directobject!="" and pinp.indirectobject!="":
    aux = [c.name for c in Misteria.getCharactersByLocation(mycharacter.location) if c.name!=mycharacter.name]
    mess = classes.Message(mycharacter.name,pinp.directobject,aux, pinp.indirectobject)
    file = open('messages','wb')
    pickle.dump(mess,file)
    file.close()
    messsig()
    print("You tell "+ pinp.directobject +": "+pinp.indirectobject)
      

  if pinp.verb=="Take":
   if pinp.directobject in myobjectnames:
    Misteria.take(name,pinp.directobject)
    print("You take the "+ pinp.directobject +".")
   else:
    print("You cannot do that.")

  if pinp.verb == "Drop":
   if pinp.directobject in Misteria.getCharacterByName(name).inventory:
     Misteria.drop(name,pinp.directobject)
     print("You drop the "+pinp.directobject +".")
   else:
    print("You cannot do that.") 


  if inp=="E":
   l = Misteria.move(name,"east")
   if l!="":
    print("You go east...")
    look(l)
   else:
    print("You cannot go that way.")
  if inp=="W":
   l = Misteria.move(name,"west")
   if l!="":
    print("You go west...")
    look(l)
   else:
    print("You cannot go that way.")
  if inp=="S":
   l = Misteria.move(name,"south")
   if l!="":
    print("You go south...")
    look(l)
   else:
    print("You cannot go that way.")
  if inp=="N":
   l = Misteria.move(name,"north")
   if l!="":
    Misteria.getCharacterByName(name).location = l
    print("You go north...")
    look(l)
   else:
    print("You cannot go that way.")
  actupdate(Misteria)
  universalsig()


def login():
 global mycharacter
 nm = input("Name of character: ")
 mycharacter = Misteria.getCharacterByName(nm)
 if mycharacter== False:
  print("Character does not exist.")
  return
 pss = input("Password: ")
 if mycharacter.password==pss:
  mycharacter.loggedOn = True
  print("")
  print("Entering the Realms of Misteria...")
  print("")
  print("Type (H)elp for command list.")
  print("")
  register()
  Misteria.getCharacterByName("Ella_the_Librarian").loggedOn=True
  actupdate(Misteria)
  universalsig()
  look(mycharacter.location)
  mainloop()
  return
 else:
  print("Wrong password.")
  return
 return

log=True
while(log):
 inp = input("#> ")
 
 if inp=="C":
   createcharacter()
 if inp=="L":
   login()
 if inp=="E":
   log=False
