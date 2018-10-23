s = "i am muskan"

def printWords(s):
    s_splitted=s.split(' ')
    #print s_splitted
    for i in s_splitted:
        if len(i)%2==0:
            print i


printWords(s)