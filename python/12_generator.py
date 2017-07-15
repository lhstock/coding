#coding:utf-8
#非波拉契数列
def fib_(max):
	n , a ,b = 0,0,1;
	while n<max:
		print b;
		a,b = b,a +b;
		n += 1;
a = fib_(5);
#定义生成器(generator)
def fib(max):
	n,a,b = 0,0,1;
	while n<max:
		yield b;
		a,b = b,a+b;
		n+=1;
b = fib(5)
print b;
#通过next调用；
# print b.next()
# print b
#通过for输出
for a in b:
	print a;

	