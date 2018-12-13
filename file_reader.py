import os

f = open('./statuslog.txt','r+')
content = f.readline()
print(content)
for i in content:
    print(i)

