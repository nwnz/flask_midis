import os
tree = os.walk(top='./cats',topdown=True)
a = list()
for i in tree:
    a= i[2]
b = list()
count = 0
for i in a:
    b.append([count,i])
    count += 1
print(b)