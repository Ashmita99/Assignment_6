myl=[4,'Arnav',1.5]
from collections import defaultdict
d=defaultdict(list)
for x in myl:
    d[type(x)].append(x)
    s= d[int]
    l= d[str]
    z= d[float]
print(s)
print(z)
print(l)