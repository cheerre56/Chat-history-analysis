import numpy as np
import collections
id = []
path = 'LINE_Podcast.txt'
with open(path, encoding='utf-8') as f:
    for line in f.readlines():
        s = line.split('	')
        b = s[1:2]
        id.append(b)
path = 'all_user.txt'
f = open(path, 'w',encoding='utf-8')
id = str(id)
id = id.replace("['","")
id = id.replace("']","")
id = id.replace('["',"")
id = id.replace('"]',"")
id = id.replace('[], ',"")
id = id.replace('[""], ',"")
id = id.replace(' ,',"")
f.write(id)
f.close()

path = 'all_user.txt'
with open(path, encoding='utf-8') as f:
    s = [i[:-1].split(', ') for i in f.readlines()]

abit = np.array(s)

unique, counts = np.unique(abit, return_counts=True)

ans=str(dict(zip(unique, counts)))
ans = ans.replace("'","")
ans = ans.replace(',',"\n")
print(ans)
f = open(path, 'w',encoding='utf-8')
f.write(ans)
f.close()