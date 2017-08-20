#coding:utf-8
a = range(1,12);
b = "abcdefghijk";
print len(a),len(b);
print a,b;
c = [x*x for x in a]
print c
d = [x+x for x in b]
print d

print a,c
#for for 
#str + int 需转换
e = [ str(x) + y for x in a for y in b]
e2 = [ '%s' %x + y for x in a for y in b]
print e
print e2

#for if 相当于嵌套
e4 = [ '%s' %x + y  for x in a  for y in b if x % 2 == 0]
e3 = [ '%s' %x + y  for x in a if x % 2 == 0 for y in b ]
print e3 ,'\n',e4,'\n',e3 == e4

import os
f = [d for d in os.listdir('.')]
print f
print  isinstance(a,list)
