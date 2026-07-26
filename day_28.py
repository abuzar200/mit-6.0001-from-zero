#list over lists over list
def list_list(warm):
    hot=["red"]
    brightcolours=[warm]
    brightcolours.append(hot)
    print(brightcolours)
    hot.append('pink')
    return [brightcolours,hot]

warm =[ "yellow","orange","white"]
print(list_list(warm))

#mutating a list while iterating over it
def remove_dups(L1,L2):
    for i in L1:
        if i in L2:
            L1.remove(i)

def remove_dups_new(L1,L2):
    L1_copy=L1[:]
    for i in L1_copy:
        if i in L2:
            L1.remove(i)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1, L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)
