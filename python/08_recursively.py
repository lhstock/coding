#coding:utf-8
def fact(n):
	if n == 1:
		return 1;
	return n * fact(n-1);
a = fact(5);
print a;
#尾递归 可解决；但是！！！大多数编程语言没有做优化；所以依旧会栈溢出
#以下为尾递归思路
def fact_(n):
	return fact_iter(n,1);

def fact_iter(num,product):
	if num == 1:
		return product;
	return fact_iter(num - 1,num * product)
b = fact_iter(1000,1);
c = fact_(900)
print b ,'\n',c ;