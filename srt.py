data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

#print new_list

s = [3, 6, 4, 5, 2, 1, 7, 8, 11, 12]
for k in range(len(s)):
    for m in range(len(s)-1):
        if s[m]<s[m+1]:
            s[m],s[m+1] = s[m+1],s[m]
print s
