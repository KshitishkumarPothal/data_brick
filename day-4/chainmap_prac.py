#group multiple dictonary into a single view
from collections import ChainMap
dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
cm = ChainMap(dict1,dict2)
print(cm)
print(cm['b'])
print(cm['c'])

cm['b'] = 6
print(cm)
