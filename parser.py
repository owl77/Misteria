
class sentence:
 def __init__(self, verb):
  self.verb = verb
 directobject = ""
 indirectobject = ""


def trim(string):
 if len(string)==1:
  return string
 if string[0]==' ':
  return string[1:]
 if string[len(string)-1]==' ':
  return string[0:len(string)-1]
 x = [m for m in range(0,len(string)-1) if string[m:m+2]=="  "]
 if x!=[]:
  return string[0:x[0]]+string[x[0]+1:len(string)]
 return string

def purge(string):
 out = trim(string)
 while(out != trim(out)):
   out = trim(out)
 return out

def preparse(string):
 if string=="":
  return sentence("")
 string = purge(string)
 aux = string.split(' ')
 prep = [a for a in aux if a=="to"]
 if len(prep)>0:
  aux[0] = aux[0]+"_to"
  aux.remove("to")
 out = sentence(aux[0])
 if len(aux)==2:
  out.directobject= aux[1] 
 if len(aux)> 2:
  out.directobject= aux[1]
  out.indirectobject=(' ').join(aux[2:])
 return out

