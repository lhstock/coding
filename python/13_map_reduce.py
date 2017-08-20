#coding:utf-8
#map
def c3(x):
	return x*3;
a = map(c3,range(10));
print a;

#reduce
#reduce(f,list) === f(f(...len-1...f(f(list[0],list[1]),list[2])....list[len-1])
def c(a,b):
	return a*b;
b = reduce(c,[1,2,3,4,5])
print b;

# [1,3,5,7,9] ==> 13579
def sh(a,b):
	return a * 10 + b;
c = reduce(sh,range(1,10)[: : 2])
print c

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
def guifan(a):
	return a.capitalize();
d = map(guifan,['adam', 'LISA', 'barT'])
print d;
name = ['adam', 'LISA', 'barT'];
#等价
e = [x.capitalize() for x in name]
print e

# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(list):
	def p(a,b):
		return a * b;
	return reduce(p,list);
f = prod(range(1,5))
print f;
