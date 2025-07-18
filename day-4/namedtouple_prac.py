from collections import namedtuple

pt = namedtuple('pt',['x','y'])
p = pt(10,20)
print(p.x,p.y)