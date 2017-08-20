#coding:utf-8
a = range(10);
for item in a:
	print item;
def for_(obj):
	for item in obj:
		 print item
for_(a);
b = 'abcdefg';
for_(b);
c = {"a":1,"b":2,"c":3}
for_(c)
# dict for  value
for value in c.itervalues():
	print value
#dict for key value
for key,value in c.iteritems():
	print key,value

#不可以 list
#for key,value in ['a','b']:
#	print key,value

from collections import Iterable
print isinstance(a,Iterable)