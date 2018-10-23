lines = []
line_odd=''
with open("abc.txt", 'r') as fh:
    for i in fh.readlines():
        lines.append(i)

print "lines : ",lines

with open("xyz.txt", 'wb') as fr:
    for i in lines:
        if lines.index(i) % 2 != 0:
            line_odd = i
            fr.write(str(line_odd))
    print(line_odd)

fr.close()
fh.close()
