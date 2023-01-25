import numpy as np
id = []
path = 'test.txt'
with open(path, encoding='utf-8') as f:
    for line in f.readlines():
        s = line.split('	')
        b = s[1:2]
        id.append(b)#215528
path = 'output.txt'
f = open(path, 'w',encoding='utf-8')
lines = str(id)
f.write(lines)
f.close()