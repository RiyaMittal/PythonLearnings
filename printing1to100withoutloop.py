add_list=[]

def printlist(num):
    if num>0:
        add_list.append(num)
        printlist(num-1)
    return sorted(add_list)


print printlist(10)
