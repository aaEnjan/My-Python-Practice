# 1.函数 含义:将独立的代码块组织成一个整体,使其有特殊功能的代码集,在需要的时候再去调用
#作用:提高代码的重要性,使代码整体看上去更加简练
#基本格式 定义函数
# def 函数名():
#     函数体
#2.调用函数
#函数名()
# def login():
#     print('这是登录函数')
# login() #调用函数
def say_hello():
    print('hello,你好,sawadika,嘿嘿')
say_hello() #调用函数前,必须保证函数已经存在
#3.返回值 函数执行结束后,最后给调用者的一个结果
#作用,return会给函数的执行者返回值
def black():  #return 函数中遇到,下方的代码不会被执行
    return '这是返回值',20 #('这是返回值', 20) return返回多个值会以元组的形式
print(black()) #一个返回值没有回返回None,一个返回值就返回一个值,多个返回值以元组形式返回给调用者
#return和print的区别:
#1.return表示此函数结束了,print会一直执行
#2.return是返回计算值,print是打印结果
def add():
    a = 1
    b = 2
    # return a+b
    print(a+b)
# print(add())
add()
#上下两种写法
def add():
    a = 1
    b = 2
    return a+b
print(add())

#3.参数  形参&实参
# def 函数名(形参1,形参2):
    #函数体
# 函数名(实参1,实参2)
def add(a,b):
    return a+b
print(add(1,3))  #a和b就是形参,1和3就是实参
#3.1 函数参数
#必备参数(位置参数) 含义:传递和定义参数的顺序及个数必须一致
#格式: def add(a,b):
def funa(name,name2,name3):
    print(name)
    print(name2)
    print(name3)
funa('czj','scy','csc') #写了几个形参,就传几个实参,不能多也不能少,顺序也是一致的
#3.2默认参数 含义:为参数提供默认值,调用函数时可不传默认参数的值
#所有的位置参数必须出现在默认参数前,包括函数定义和调用
#格式: def funb(a=66):
def funb(b,a=88):
    print(a,b)
# funb() #a=88就是默认值,没有传值就根据默认值来执行代码
funb(100,200) #100就是传入的实参,传值就会根据传入的值来执行代码
#3.3 可变参数 含义: 传入的值数量是可以改变的,可以传入多个,也可以不传
#格式 def func(*args):
def func(*args):
    print(args,type(args))
func('漩涡鸣人','宇智波佐助','撒库拉酱')  #以元组形式接收
#关键字参数 **kwargs
def fund(**kwargs):
    print(kwargs,type(kwargs))
fund(name='曹振江',age=18) #{}  返回字典dict  空集合是set{}
#4.函数嵌套 含义
#4.1嵌套调用    在一个函数中调用另一个函数
def dinner():
    print('晚上吃火锅')
def sleep():
    dinner() #在sleep函数中调用dinner函数
    print('吃完火锅睡觉了')
sleep()
#4.2 嵌套定义    在一个函数中定义另一个函数
def water():
    print('每天喝2L水')
    def eat():
        print('也要吃东西的')
    eat()  #注意所以 定义和调用是同级的
water()
# 每天喝2L水
# 也要吃东西的   执行顺序是根据代码顺序执行的 需要注意:不要在内层函数中,调用外层函数,会陷入死循环,直到超过递归的最大深度 eat是内 water是外, eat前不能调用water

# 作用域 含义:指的是变量生效的范围,分为两种,分别是全局变量和局部变量
#全局变量  函数外部定义的变量,在整个文件中都是有效的
a = 100 #这就是一个全局变量
def test1():
    print('这是test1中函数的值',a)
# test1()
def test2():
    b = 120 #这里就是局部变量,从定义位置开始到函数结束位置有效
    print('这是test1中函数的值',b)
test1() #函数内部没有a的值,在外部有定义a = 100
test2() #在函数内部找到了是120
#在函数内部修改全局变量的值,可以实例'global'关键字  将变量声明为全局变量  global 变量名 有多个变量 global 变量1,变量2,变量3
def funa():
    global six,age
    six = 666
    age = 19
    print(six,age)
funa()
print(six,age)
#nonlocal  不是本地  用来上声明外层的局部变量,只能在嵌套函数中使用,在外部函数先进行声明,内部函数进行nonlocal声明
a = 666
def hsw():
    a = 777
    def hsn():
        nonlocal a
        a = 888
        print(f'这是hsn的值:{a}')
    print(f'这是hsw为被nonlocal声明的值:{a}')
    hsn()
    print(f'这是hsw被nonlocal声明后的值{a}')
hsw()
#匿名函数 基本语法: 函数名 = lambda 形参:返回值(表达式)
#调用 结果 = 函数名(实参)
def funz(b):
    return a+b
print(add(1,2))

#匿名函数写法 可以简化代码
add = lambda a,b:a+b #a , b 就是你们函数的形参,a+b就是返回值的表达式
#lambda不需要写return来返回值,表达式本身结果就是返回
print(add(1,5))
#无参数
funf = lambda : '爱喝蜜雪冰城'
print(funf())
#一个参数
fung = lambda name:name
print(fung('曹振江'))
#默认参数
funh = lambda name,age=18:(name,age) #多个参数用元组()
print(funh('曹振江',25))

funj = lambda a,b,c=3:a+b+c
print(funj(1.2,2)) #不穿c实参也可以 因为c有默认值
# print(funj(1.2)),没有b就会报错  默认参数必须协作非默认参数后边
#关键字参数
funk = lambda **kwargs:kwargs
print(funk(name='czj',age=18)) # {'name': 'czj', 'age': 18} 返回字典
#lambda的应用, 结合if判断
a = 8
b = 6
print('正确') if a<b else print('错误')
# 如何结合
funl = lambda a,b:'正确' if a<b  else '错误'
print(funl(5,8))
#lambda只能实现简单的逻辑,如果逻辑复杂且代码量较大,不建议使用,降低代码的可读性

#内置函数 python中已经定义好的函数,如何查看呢?
# 查看所以的内置函数 大写字母开头一般是内置常量名,小心字母开头是内置函数名
# import builtins
# print(dir(builtins))
#abs 返回绝对值
print(abs(-3)) #返回 3
#sum(): 求和  内要放可迭代对象,和数字
print(sum([1,2,3,4]))
print(sum({1,2,3,}))
print(sum((1,2.0,)))
# print(sum(('1.2','0',))) #字符串不可以
#min() max() 求最小和最大值
li = [1,23,4,65,341]
print(max(li))
print(min(li))
print(min(-5,4,key=abs))
#zip() 将可迭代对象作为参数,将对象中对应的元素打包成一个个元组
li = [1,2,3]
li2 = ['a','b','c','d']
print(zip(li,li2))
for i in zip(li,li2):
    print(i,type(i))
#第二种方式,转换成列表打印
li = [1,2,3]
li2 = ['a','b','c']
print(list(zip(li,li2)))
#map() 也称为映射函数,可以对可迭代对象中每一个元素进行映射,分别去执行
#map(func,iter):  func 自己定义,iter 放入的可迭代对象

li = [1,2,3]
# def funr(x):
#     return x * 3
# mp = map(funr,li) #只要写函数名,不需要写()

funr  = lambda x:x + 3
mp = map(funr,li)
print(list(mp))

# print(mp) #<map object at 0x0000023F169C55B0> 输出一个对象,可以用for循环取出来
# # for i in  mp:
# #     print(i)
# #也可以转换成列表
# print(list(mp))

#reduce(): 先把对象中的两个元素取出来,计算一个值保存,然后计算的值跟第三个元素进行计算
#需要先导包 from functools import reduce
from functools import reduce
#reduce(function,sequence) # function - 必须是有两个函数的参数, sequence = 序列:可迭代对象
li3 = [1,2,3,4]
def add(x,y):
    return x + y
res = reduce(add,li3)
print(res)  #打印为10  1+2=3 3变x,然后3+3=6 6变x,然后6+4=10
#拆包:对于函数中的多个返回数据,去掉元组,列表或字典,直接获取里面数据的过程
tua = (1,2,3,4)
a,b,c,d = tua
print('a=',a,'b=',b,'c=',c,'d=',d)
#要求元组内的个数与接收的个数相同,对象内有多少个数据,就需要定义多少个变量接收
# a,b = tua #报错 值错误,要拆包的值过多,没有足够的变量名去定义,一般去获取元组值的时候使用
#
a,*b = tua
print('a=',a,'b=',*b)
#一般在函数调用时使用,
def funq(a,b,*args):
    print(a,b)
    print(args,type(args))
funq(1,2,3,4,5,6,7)
#先把单独的取完,剩下的交给带*号的变量











