#coding:utf-8

#默认参数
def power(num,n=2):
	a = 1;
	while n > 0:
		a = a * num;
		n = n -1;
	return a;
a = power(2);
b = power(3,3);
print a ,b;

#定义不可变参数
def addEnd(s = None):
	if s is None:
		s = [];
	s.append('End');
	return s;
	#对比可变参数
def addEnd_(s=[]):
	s.append("End");
	return s

a_ = addEnd_();
b_ = addEnd_();
c_ = addEnd_(['c']);

a = addEnd();
b = addEnd();
c = addEnd(['c']);
print a_,b_,c_,a,b,c;

#定义可变参数 (数量？)
	#若是要累加许定义一个list or tuple
def cale_(list):
	num = 0;
	for item in list:
		num = num + item;
	return num;
list = [1,3,4]
a = cale_(list);
print a;

	#改善；
def cale(*number):
	num = 0;
	for item in number:
		num += item;
	return num;
a = cale(1,3,4);
print a;

import json
#关键参数 会把多个多余参数转为dict；也可定义一个dict为关键参数
def person(name ,**kw):
	print 'name:',name,'other:' ,json.dumps(kw,encoding='UTF-8',ensure_ascii=False)
person(u'张三')
person(u'张三',like =u'吃喝玩乐')
person(u'张三',like =[1,3,4])

a = {"name":"张三"}
print json.dumps(a,encoding="UTF-8",ensure_ascii=False)
b = ['张三','李四']
print json.dumps(b,encoding='UTF-8',ensure_ascii=False)
print b


#可在调用时通过*,** 指定;
#但是 *的参数会顶替必须参数；
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
args = (1, 2, 3, 4, 5)
args2 = {"x":1,"y":2}
kw = {'x': 99}
func(*args, **kw)
func(args,*(2,), **kw)