#day2 - 循环语句 : 重复的做一件事  钟表...
a = 1
while a <= 10:
    print(a,"好好学习,天天向上")
    a += 1
else:
    print(a,"不要学了")

# #死循环写法
# while True: #条件只写true,说明条件一直为真,就会一直执行,从而形成一个死循环
#     print("循环执行")

#while循环应用:计算1+2+3+....+100的值
r = 1
value = 0
while r <= 100:
    value += r
    r += 1
else:
    print(value)
#while循环嵌套: while内还有while

a = 1
while a <= 3:
    print(f'这是第{a}次外循环')
    b = 1
    while b < 10:
        b += 1
        print(f'这是第{b}次内循环')
    a += 1
else:
    print("循环结束")

#for 循环
#基本格式 for 临时变量 in 可迭代对象:
        # 循环满足条件时执行的代码,注意冒号和缩进
# str = 'hellp python'  #遍历
# for r in str:
#     print(r)

#range()计数
r = 1
for i in range(1,11): #从1开始,从11介绍 [1,11)
    r += 1
    print(i,r)
#for循环1+2+3..+100
o = 0
for i in range(1,101):
    o += i
print(o)
#相比之下 for循环比while更简便一点,更常见

#break中途退出结束循环和continue结束当前循环,进入下一循环
s = 0
for i in range(1,101):
    s += i
    print(i, s)
    if s > 100:
        break
print(i,s)

#continue 跳过当前循环,进入下一循环
L = 0
while L <= 5:
    print(f"在吃第{L}个")
    if L == 3:
        print(f'不吃了已经吃到了第{L}个')
        L += 1
        continue
    L += 1




