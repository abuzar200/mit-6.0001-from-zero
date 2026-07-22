# list operations part 1

def list_op(l1,l2):

    l1.append(6)
    l1.remove(3)
    del(l2[1])
    l2.remove(2)
    l2.remove(5)
    l2.extend([8,10,12])
    l3=l1+l2
    print(l2.pop())
    print(l2.pop(1))
    return l1,l3

l1=[2,4,3]
l2=[5,43,2]
print(list_op(l1,l2))
