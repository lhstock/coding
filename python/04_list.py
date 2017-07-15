#coding:utf-8
list = ['A','B','c','d'];
print list[0];
print list[1];
print list[2];
print list[3];
print list[-1];
print list[-2];
print list[-3];
print list[-4];
list.append('e');
list.insert(3,'f');
print list ,len(list);
list.insert(6,'ff');
print list ,len(list);
list.pop();
print list;
list.pop(3);
print list;
#len(list=5) list[5]只能通过append添加；否则越界
#list[5] = 'f';
#print list