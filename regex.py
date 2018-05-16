import re
"""
fh=open("tags.html")
for i in fh:
    reg=re.search(r"<([a-z]+)>(.*)</\1>",i)
    print (reg.group(1) + ":" + reg.group(2))


s="Sun Oct 14 13:47:03 CEST 2012"
expr=r"(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)"
x=re.search(expr,s)
print x.group('hours')
print x.group('minutes')
print x.group('seconds')
"""

hw=open("Highway_info.txt")
for i in hw:
    expr=r"^([A-Z]{2})\s(.*)"
    res=re.search(expr,i)
    print (res.group(1) + " --> "+ res.group(2))