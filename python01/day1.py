#1.1算数运算符
print(1+1)
print(1-1)
print(1*1)
print(1/1) #注意:商一定是浮点数,分母不能为0
a = 1/1
print(type(a))
#1.2 //取整除,向下取整,不管四舍五入的原则
print(14//5)
b = 30/9
print(b)
c = 30//9
print(c)
#1.3 % 取余数
print(9%3)
print(8%3)
#1.4取幂 **
print(2**4) #2*2*2*2=16
#1.5使用算数运算符,有浮点数则结果也会有浮点数表示
print(15.0+3)
#1.6加减乘除优先级排序,幂>乘>除>取余....>加减

#2.0赋值运算符 给变量赋值
num1 = 5
num2 = 8
#2.1将一个变量的值赋给另一个变量
num3 = num1
num4 = num2
print("第2章2.0:",num3,num4)
print("5+8=",num3+num4)
#2.2 +=
a = 3
a += 1 #等效于a+1
print(a)

n1 = 99
n2 = 66
# n1 = n1 + n2
n1 += n2 #等效余n1 = n1 + n2
print("售卖价",n1)
#同理 -=   赋值运算符不能用于纯数字
print(n1,n2)
n1 -= n2
print(n1)

#3.0 input()  输入函数
# name = input("输入:姓名")
# print(name)
# uesrname = input("输入账号")
# pwd = input("输入密码")
# print(uesrname,pwd)

#4.0 转义字符
#4.1 \t 制表符,通常表示四个字符,也成缩进
print('sixs\thha')
print('姓名\t年龄\t电话')
#4.2\n换行符
print('曹振江\n帅的换行')
#4.3\r 回车 将当前位置移到本行开头
print('哈哈哈\r嘿嘿')
#4.4\\ 反斜杠符号
print('aa\\bb\\cc\\dd')
#4.5 r 原生字符串,取消转义
print(r'a\tc')

# 5.0 if判断
# age = input("输入年龄")
# if age < "18":
#     print('未成年不能上网')
# 小练习
# chengji = input('输入你的成绩:')
# if chengji == "100":
#     print("你真棒")
# if chengji == "60":
#     print('还要继续加油啊')

#运算符
# 比较运算符 == != > < >= <=
a = 111
b = 222
print("不相等返回真",a!=b)
print("a不大于b返回假",a>=b)
# 关系运算符 and or not
a = 'czj'
b = 'jzc'
if a == 'czj' and b == 'jzc':
    print("这是真的and")
if a == 'czj' or b == 'jzc1':
    print("这是真的or")
if not b == 'jzc1':
    print("这是真的not")
print(not 1>3) #1不大于3 但是用的not 所以返回True

#if else  if elif  if elif else
a = 777    #a = 666
if a == 666:
    print('你真棒')
elif a == 777:
    print('你微微棒')
else:
    print('继续加油')

a = 9 #input('输入a的值')
b = 8 #input('输入b的值')   输入后再比较,再print
if a <= b:
    print('a比b小')
else:
    print('a比b大')

# a = input('输入一个数字')    #a = 666
# if a > '666':
#     print('你真棒')
# elif a == '666':
#     print('你微微棒')        
# else:
#     print('继续加油')

#if嵌套  if内还有if
num = True
# zhengchang = 36.5
zhengchang = float(input('输入'))
if num == True:
    print("有车票可以上车")
    if 36.2 <= zhengchang <= 37.2:
        print('体温正常,可以上车')
    else:
        print('不太正常,去隔离或再出示健康码')






















