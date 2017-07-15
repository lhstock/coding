#coding:utf-8
#测试换行定义是否错误；
dict = {'liu':5,'zhang':7};
print dict;
dict2 ={
	u'刘':dict['liu'],
		u'张':dict['zhang']
};
#汉字 key 和 u转码的汉字key是否一致
print dict2;
t1 = u'刘' in dict2;
t2 = '刘' in dict2;
print u'输出t1' , t1
print u'输出t2' , t2

#get获取
get1 = dict2.get('刘');
get2 = dict2.get('刘',22);
print get1;
print get2;

#pop删除
dict2.pop(u'刘');
print dict2;


#key 必须为不可变对象；
d = {}
arr = ['a','b','c'];
for sub in arr:
	d[sub] = sub;
print d , arr;
arr[1] = 'd';
print d , arr;
#那么可变对象呢
arr2 = ('a','b','c')
for sub in arr2:
	d[sub] = sub;
print d , arr2;
z = {arr2:3}
print z
arr3 = ('a',['b']);
#arr3不为不可变对象
# zz = {arr3:4}
# print zz

# arr2[1] = 'd';
# print d , arr2;