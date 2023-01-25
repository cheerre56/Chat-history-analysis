import collections, numpy
path = 'testdata.txt'
with open(path, encoding='utf-8') as f:
    s = [i[:-1].split(', ') for i in f.readlines()]

abit = numpy.array(s)

unique, counts = numpy.unique(abit, return_counts=True)

print(dict(zip(unique, counts)))