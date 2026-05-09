# before this you learned creating virtual environment 
# how to create virtual environment
#if you are on windows first check python version by python --version
# then py -3.14 -m venv env (this command creates virtual environment named env)
# to activate venv .\env\Scripts\Activate.ps1 use this command
# to deactivate just type deactivate

# list is a collection of different data types and stores in square brackets [int,str,bollean,float]
# list = ["a",1.2,false,23]

# Data structures 1) list 2) dictionary 3)set 4) tuple
 
a=[100,200,True,3.5] # 1st type making list
 
a.append(500)
print(a)
#output
# ython lists.py
# [100, 200, True, 3.5, 500]
# PS C:\you work\python\practise>

clouds = list(("aws","azure","zoho","gcp","utho","ibm")) # 2nd type of making list 

print(clouds)
print("length of list is :",len(clouds))
print("world leader for cloud service provider is :",clouds[0])
print("the last name in the list is :", clouds[-1])

print(dir(clouds)) # what dir does is this tells you what all you can do
# with this list 

#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(clouds.count.__doc__) # this Return number of occurrences of value

print(clouds.__add__) #<method-wrapper '__add__' of list object at 0x000001D88E4BE840>

for i in clouds:
   print (i)