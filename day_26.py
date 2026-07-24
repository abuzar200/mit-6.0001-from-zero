#list operations part 2
def list_op(s):
    print(list(s))
    print(s.split(">"))
    print(sorted(s))
    s=list(s)
    s.sort()
    s.reverse()
    return s

s="I>s c akne"
print(list_op(s))
