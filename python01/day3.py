#字符串常见操作
#1.查找相关
#find(子字符串,开始下标,结束下标) 查找 检测某个子字符串是否包含在字符串中,在就返回开始位置的下标,否则就返回-1
name = 'caozhenjiang'
print(name.find('j'))
print(name.find('c'))
print(name.find('e',6,9))
#index() 和find的区别就是找不到会报错,find会返回-1
print(name.index('o',1,9))
#count():返回某个字符串出现的次数,没有就返回0
print(name.count('a',1,19))

#判断相关
#1.startswith():判读是否以某个字符串开头,是返回true,不是的话返回false,如果设置开始和结束位置则在指定范围内查找
print(name.startswith('aozhe',1,9))
#2.endswith():判读是否以某个字符串结尾,是返回true,不是的话返回false,如果设置开始和结束位置则在指定范围内查找
print(name.endswith('jiang',1,12))
#3.isupper():检测字符串中所有字母是否都是大写,是true,不是falase
str = 'SIXSIX'
print(str.isupper())
print('teS'.isupper())

#修改相关
#1.replace(旧内容,新内容,替换次数):替换
name = '好好学习,天天向上天天天'
print(name.replace('天','帅',3))
#2.split():指定分隔符来切字符串
str = 'hello,python,mynameisczj'
print(str.split(',')) #指定 , 是分隔符
print(str.split('f')) #没有分隔符就整体返回
print(str.split(',',1)) #分隔1次
#3.capitalize():第一个字符大写
print(str.capitalize())
#4.lower():大写字母转为小写   upper(): 小写字母转成大写
str = 'HELLO,PYTHON,mynameisczj'
print(str.lower()) #大写转小写
print(str.upper()) #小写转大写

#列表 基本格式
#列表名 = [元素1,元素2,元素3...] 所以元素放在[]中间,用,隔开 ,列表是可迭代对象,可以for循环,遍历取值
li = [1,2,3,4,5,6,7,'a',9,10]
# print(type(li))
# print(max(li)) , print(min(li))
# print(sum(li))
print(li[0:10]) #包前不包后
for i in li:
    print(i)
#列表相关操作,增删改查,排序 常见操作
#添加元素 append() extend() insert()
li = [1,2,3,4,5,6,7]
li.append('第八'),print(li) #append整体添加
li.extend('第八'),print(li) #append分散添加
li.insert(3,'第八',),print(li) #insert在指定位置添加元素,原有元素往后
li = [1,2,3,4,5,6,7,'a',9,10]
# li.extend(0) #报错
li.insert(3,0)
print(li)
#修改元素 直接通过下标就可以进行修改
li = [1,2,3]
print(li[1])
li[2] = 4
print(li)
#查找元素 in 判断指定元素是否存在列表中,存在返回true,不存在就返回false   not in 相反  不存在返回true,存在返回false
li = ['a','b','c']
print('b' in li)
print('d' in li)
print('b' not in li)
print('d' not in li)

#用户输入昵称,昵称重复则不能使用  小练习
# while True:
#     username = ['曹振江','孙成玉']
#     name = input('请输入你想用的昵称')
#     if name in username:
#         print(f'昵称{name}已经被使用,请更换其他昵称')
#     else:
#         username.append(name)
#         print(f'昵称使用成功新增{name},当前已经存在的昵称有{username}')
#         break
name = [1,2,3,4,5,6,3,4,5,3]
print(name.index(3))
print(name.count(3))
#删除元素 del
li = ['a','b','c','d']
del li[2] #根据下标删除  del li 删除列表
print([li])

#pop 删除指定下标的数据,python3版本默认删除最后一个元素,下标不能超出范围
li.pop()
print([li])
li = ['a','b','c','d','c']
li.pop(0)
print([li])

#remove根据元素的值进行删除
li.remove('c') #如果有多个,会删除第一个
print([li])

#列表排序 sort 将列表按特定顺序重新排列,默认从小到大
li = [1,3,4,5,73,13,4,63,11,6,2,65,123]
li.sort()
print([li])
#reverse() 列表倒序从后到前
li = [1,3,4,5,73,13,4,63,11,6,2,65,123]
li.reverse()
print([li])
#将两种方法结合就可以从大到小排序
li = [1,3,4,5,73,13,4,63,11,6,2,65,123]
li.sort()
li.reverse()
print([li])
#列表推导式 格式1:[表达式 for 变量 in 列表]  in后面不仅可以跟列表,也可以放range() 可迭代表达式
# li = [1,2,3,4,5,6,7,8,9]
# [print(i*5) for i in li]

li = []
for i in range(1,6):
    li.append(i)
print(li)

li = []
[li.append(i) for i in range(1,10)]
print(li)

#格式2 [表达式 for 变量 in 列表 if 条件]
#把奇数放在列表里面
li = []
for i in range(1,11):
    if i % 2 == 1:
        li.append(i)
print(li)

li = []
[li.append(i) for i in range(1,11) if i % 2 ==1]
print(li)

#列表嵌套
#含义 一个列表里有另一个列表
li = [1,2,3,[4,5,[7,8],6]] #[4,,5,6]是里边的列表  代表下标为3
print(li[3])
print(li[3][2][0]) #

#3.元组基本格式 tua = (1,2,3,4)
#元组
tuple = (1,2,3,4,'a',[1,2,3])
print(type(tuple))
print(tuple[3],tuple[4],tuple[5]) #输出下标3  为4

tua = (1,) #只有一个的时候为int  加 , 才是元组 tuple
print(type(tua))
#元组不允许修改,只支持查询操作
tua = (3,2,1,4,5)
# tua[2] = 1 #不支持修改  运行会报错
print(tua)
#count() index find len 跟列表用法相同
print(tua.count(1)) #查询1有1个
print(tua.index(5)) #查询5 在第4个下标
print(len(tua)) #有5个
#应用场景  函数的参数和返回值
name = 'sunchengyv'
age = 18
print('姓名和年龄',(name,age))
c = (name,age)
print(type(c))   #打印出c这个变量就是元组
print('姓名和年龄',c)
#数据不可以被修改的情况下使用,保护数据的安全性

#字典格式  基本格式 字典名 = {'key1':'value1','key2':'value2'}
dict = {'name':'sunchengyv','age':18}
print(type(dict))
#字典的常见操作,增删改查
#查询元素 变量名[键名]  字典中没有下边,查找需要找键名
print(dict['name'],dict['age'])
#变量名.get(键名)
print(dict.get('name'))
print(dict.get('nam','不存在')) #如果查不到返回自己设置的键名
#修改元素
dict['name'] = 'caozhenjiang'
print(dict['name']) #列表通过下标,字典通过键名修改
#添加元素
#变量名[键名] = value  注意 存在就修改,不存在就新增
dict['gender'] = 'man'
print(dict)
dict['gender'] = 'women'
print(dict)
#删除元素 del 删除全部 del dict  直接删除整个字典
del dict['name']
print(dict)

#clear(): 清空整个字典内的内容,但保留字典
dict.clear()
dict['name'] = '曹振江'
print(dict)
#pop()删除指定键值对,键不存在既报错
dic = {'name':'sunchengyv','age':'18','gender':'man'}
dic.pop('age')
print(dic)
#字典的场景操作 二  len() 求长度
print(len(dic)) #2 有两个键值对 kv对
#keys() 返回字典里面包含的所以键名
print(dic.keys())
for i in  dic.keys():
    print(i)
#values()
print(dic.values())
for i in  dic.values():
    print(i)
#items():返回字典里面包含的所有键值对,键值对以元组形式
for i in dic.items():
    print(i)
#字典的应用场景 使用键值对存储描述一个物品的相关信息

#集合格式  集合是无需的,内的值是唯一的  集合名 = {元素1,元素2,元素3}
set = {1,2,3}  #当定义 {} type是字典 如何定义一个空集合 s1 = set()
print(set,type(set))
# s1 = set()
# print(s1,type(s1))
#集合有无序性
s1 = {'a','b','c','d','f'}
print(s1)  #每次打印都不一样,集合有唯一性,会自动去重
s2 = {7,2,3,4,5,6,2,2,3}
print(s2)
#集合的常见操作 添加add,update和删除
s3 = {1,2,3,4}
print(s3)
s3.add(5) #一次只能添加一个元素,如果已存在则不进行任何操作
print(s3)
#update
s4 = {1,2,3,4,5,6}
s4.update((7,8,9)) #可迭代对象  字符串,列表,元组
print(s4)
#删除元素 remove: 选择删除的元素,如何集合中有就删除,没有就报错
s4.remove(9)
print(s4)
#pop 直接删除
s4.pop() #默认删除排序后的第一个元素
print(s4)
s5 = {'a','b','c'}
print(s5)
s5.pop()
print(s5)
#discard:选择删除的元素,有就会删除,没有则不会发生改变,不会进行操作
s6 = {1,2,3,4,5,6,7}
print(s6)
s6.discard(5)
print(s6)

#交集和并集
#交集,共有的部分
a = {1,2,3,4,5}
b = {3,4}
print(a & b) #返回 3,4
c = {7,8,9}
print(a & c) #没有返回set()
#并集 |
a = {1,2,3}
b = {3,4,5}
print(a | b)
l = a | b
print(type(l))













