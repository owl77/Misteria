
import classes
import world
import pickle


Misteria = classes.World("Misteria")
Misteria.worldmap = world.mymap


Ella = classes.Character("Ella_the_Librarian")
Ella.description = "A shy girl with glasses who is very protective of books."
Ella.npc = True
Misteria.addCharacter(Ella)


Elf = classes.Character("Elf")
Elf.description = "Young hero out for fame and fortune."
Elf.password="123"
Misteria.addCharacter(Elf)

Zelda = classes.Character("Zelda")
Zelda.description = "Slender elven princess."
Zelda.password="123"
Misteria.addCharacter(Zelda)



Key = classes.Object("Key")
Key.description ="A large golden key with a curious engraving on it."
Key.location = "Start"
Misteria.objects.append(Key)
f = open('world','wb')
pickle.dump(Misteria,f)
f.close()

pids = []
f = open('pids','wb')
pickle.dump(pids,f)
f.close()

mess = classes.Message("","",[],"")
file = open('messages','wb')
pickle.dump(mess,file)
file.close()

