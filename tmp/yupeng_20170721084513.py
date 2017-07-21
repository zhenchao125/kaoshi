# -*- coding: UTF-8 -*-
print 'Hello Yztc!'


import this
s=this.s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print 'python 之禅' 
print "".join([d.get(c, c) for c in s])