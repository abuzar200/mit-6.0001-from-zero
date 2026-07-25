#aliasing vs clonning
def alias_1(a):
    b=a
    return a,b
def alias_2(warm):
    hot=warm
    hot.append('pink')
    return hot,warm
def clonning(cool):
    chill = cool[:]
    chill.append('black')
    return chill,cool
a=123
warm=['red','yellow','orange','blue']
print(alias_1(a) and alias_2(warm))
cool=['blue','green','grey']
print(clonning(cool))
