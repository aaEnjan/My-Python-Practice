#1.类型转换
# 1.1 int(): 转换为一个整数,只能转换由纯数字组成的字符串
a = 1.2
print(type(a),a)
b = int(a)
print(type(b),b) #浮点型强转整型会去掉小数点后边的数,只保留整型部分
#字符串转换为整型 str -> int
a = int('123')
print(type(a),a)
# b = int('123a')
print(type(b),b) #只能强转纯数字组成的字符串 如果有不是数字以外的会报错
#用户从控制台输入,判断年龄
# while True:
#     try:
#         age = int(input('请输入你的年龄: '))
#
#         if age < 0:
#             print('年龄不能为负数！请重新输入。')
#             continue  # 继续循环要求重新输入
#         break  # 输入有效，跳出循环
#     except ValueError:
#         print('输入无效，请输入纯数字！')
# # 处理有效的年龄输入
# if 100 >= age >= 18:
#     print('您成年了')
# elif age > 100:
#     print('你无敌了!')
# else:
#     print('你是未成年')
#1.2 float(): 转换为一个小数
print(float(11))
print(float(-11))
print(float('+11.334')) #如果字符串中有正负号,数字和小数点以外的字符,则不支持转换,会报错
#1.3 str(): 将对象转换为字符串类型,任何类型都可以转换成字符串
n = 100
print(type(n))
n = str(n)
print(type(n))
st = str(-1.80000) #浮点型转换为字符串,会去除末尾的0
print(type(n),st)
sr = [1,2,3]
print(type(n),sr)
#1.4 eval() 执行一个字符串表达式,并返回运算值 ,功能非常强大,但是不够安全,容易被修改数据
print(10+10)
print('10'+'10')
print(eval('10+10')) #执行运算并返回运算的值,只能同类型操作 可以实现list列表,dict字段,tuple元组和str之间的转换
st1 = '[[1,2],[3,4],[5,6]]'
print(type(st1),st1)
li = eval(st1) #str -> list
print(li,type(li))
#str -> dict
st1 = "{'name':'caozhenjiang','age':18}"
print(type(st1),st1)
dict = eval(st1) #str -> list
print(dict,type(dict))
#1.5list() 将可迭代对象转换为列表 支持转换为list的类型: 字符串str ,元组tuple,字典dict,集合set   不可迭代的对象int   可迭代对象是可以被for循环的
#str -> list
print(list('1234')) #['1', '2', '3', '4']
# tuple ->list
print(list((1,2,3,4)))
#dict -> list 字典转换成列表会取键名作为列表的值
print(list({'name':'caozhenjiang','age':18}))
#set -> list 集合转换成列表,会先去除再转换, 集合是无序的
print(list({1,2,3,4,5,'a','b',3,'d'}))
#2深浅拷贝
#2.1赋值 类似两个人吃饭做一个桌子,菜多菜少都能感受到,共享资源,一个值的改变会完全被另一个值共享
li = [1,2,3,4]
print(type(li),li)
li2 = li #将li的值直接赋值给li2
print(type(li2),li2,li)
#给li列表新增元素
li.append(5)
print(type(li2),li2,li)
li2.append(6)
print(type(li2),li2,li)
print(id(li),id(li2)) #他俩的内存地址是一样的,是同一个对象
#当拿到数据后,会对数据进行处理,显然处理后修改元数据有时候会不明智,所以有copy方法,浅拷贝和深拷贝
#2.2浅拷贝 会创建新的对象,拷贝第一层的数据,嵌套层会指向原来的内存地址,属于数据半共享
import copy #导入copy模块
li = [1,2,3,[4,5,6]]
li2 = copy.copy(li)
print(li2)
#查看内存地址 id()  内存地址不一样说明不是同一个对象,
print(id(li),id(li2))
li.append(8)
print(li,li2)
#往嵌套列表添加元素
print(li[3])
li[3].append(7)
print(li,li2) #[1, 2, 3, [4, 5, 6, 7], 8] [1, 2, 3, [4, 5, 6, 7]] 嵌套内的第一层数据是一样的内存地址
print(id(li[3]),id(li2[3])) #嵌套的第一层内存地址是相同的,但是外层的内存地址不同  及只拷贝第一层嵌套的内存
#应用场景, 优点:拷贝速度快且占用空间少,拷贝效率高
#2.3深拷贝 数据完全不共享,外层的对象和内部的元素都拷贝的一遍
li = [1,2,3,[4,5,6]]
li2 = copy.deepcopy(li) #深拷贝 只会影响本身,跟原来的对象没有关联
print(li,li2)
li.append(8)
print(id(li),id(li2))
print(li,li2) #[1, 2, 3, [4, 5, 6], 8] [1, 2, 3, [4, 5, 6]]
li[3].append(7)
print(li,li2) #[1, 2, 3, [4, 5, 6, 7], 8] [1, 2, 3, [4, 5, 6]]

#3.可变对象 含义:存储空间保存的数据允许被修改,这种数据就是可变类型  可变类型: 列表list  字典dict  集合set  变量对应的值可以修改,但是内存地址不会发生改变
list = [1,2,3,4]
print(list,id(list)) #[1, 2, 3, 4] 2510490847744
list.append(5)
print(list,id(list)) #[1, 2, 3, 4, 5] 2510490847744   内存地址没有发生改变
set = {1,2,3}
print(set,id(set))
set.add(4)
set.update('4')
print(set,id(set))
set.remove(4)
print(set,id(set))
#不可变对象 元组tuple , 字符串 str , 数值 int
n = 10
print("源地址",n,id(n))
n = 15 #修改n的值就会重新生成新的值,重新赋值给变量n
print("修改后地址",n,id(n))

str = 'a,v,c'
print("源地址",str,id(str))
str = 'caozhenjiang' #修改str的值就会重新生成新的值,重新赋值给变量str   个人理解: 不可变对象赋值时都是重新定义变量对象,所以内存地址会发生变换, 二次赋值也是 变量名= 变量值
print("修改后地址",str,id(str))

tup = (1,2,3)
print("源地址",tup,id(tup))
tup = ('a','b') #同理
print("修改后地址",tup,id(tup))









