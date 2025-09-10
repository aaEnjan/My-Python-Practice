#抛出异常 raise
# 步骤:1.创建一个Exception('xxx'),xxx - 异常提示信息 2. raise抛出这个对象(异常对象)
# def funa():
#     raise Exception('抛出一个异常信息')
#     print('哈哈哈哈哈') #会报错,执行了raise语法,代码就不会继续往下执行
# funa()

#需求 : 用户输入密码,  密码长度不足,就抛出异常
# 分析:用户输入密码,判断输入的长度是否大于等于8,如果len不足8位,就报错,即抛出自定义异常,并捕获
# def login():
#     pwd = str(input('请输入您的密码'))
#     if len(pwd) >= 8:
#         return '密码符合要求'
#     e = Exception('密码不符合要求,长度不足8位')
#     raise(e)
# # print(login())
# try:
#     print(login())
# except Exception as e:
#     print(e)
#捕获异常是为了检测到异常时,代码还能继续往下运行,即程序不会终止

#导入模块 import 模块名1,模块名2  可以导入1个,也可以导入多个 ,但最后一个模块单独使用
#调用功能方法: 模块名.功能名
# import pytest #这里的pytest代表的是pytest模块,也就是有另外的一个python.py文件   需要注意命名
#调用pytest模块中的name变量
# print(pytest.name)  #调用pytest.py文件中的name变量
# pytest.funa()
#方法二: from 模块名... import 功能1,功能2
# from pytest import funa
# funa()
# print('---------------')
#方法3 from 模块名 import *   把模块中所以的内容全部导入,不建议过多使用,命名有冲突就会有错误
# from pytest import *
# funa()
# funb()
# print(name)
# as 给模块起别名  语法: import 模块名 as 别名
#给模块起别名
# import pytest as pt
# #调用模块中的funa()
# pt.funa()
# #as 给功能起别名  语法 from 模块名 import 功能名 as 别名
# from pytest import funa as fa,name,funb as fb  #这里的name是pytest模块中定义的name变量
# fa()
# fb()
# print(name)
#注意,导入多个功能,使用,将功能与功能隔开,后面的功能也可以取别名: 功能名 as 别名

#内置全局变量 __name__  语法 : if __name__ == "__main__":
#作用 用来控制py文件在不同的应用场景执行不同的逻辑
#1.文件在当前程序执行(即自己执行自己): __name__ == "__main__"  被当做模块导入时,它下面的代码不会被显示出来
#2.文件被当做模块被其他文件导入: __name__ == 模块名

# import pytest2 as p2
# p2.test()

#1.包 含义: 就是项目结构中的文件/目录  包是含义__init__.py的文件  python package
#作用:讲有联系的模块放在同一个文件夹下,有效避免模块名称冲突问题,让结构更清晰
#2.import 导入包时,首先执行 __init__.py文件的代码  不建议在__init__.py文件中写大量代码,尽量保证文件内容简单
#__init__.py  这个文件代码主要就是导入包下的其他模块
import pack01  #导包方式1 会执行__init__.py 但是不会执行包内的模块
# from pack01 import pytest01 #导包方式2 会执行包内的模块代码 可
# pytest01.funa()
#再用导包方式1 就可以直接执行 __init__.py内的代码, 这个文件中又有导入方式2中的导入
import pack01
#3.__all__   是一个变量: 本质是一个列表,列表里面的元素就代表要导入的模块
#作用:可以控制可以引用的东西  语法 : __all__ = ['模块1','模块2']  相当于导入[]里面定义的模块
from pack01 import *
pytest01.funa()
login.log()
#包的本质依然是一个模块,包中也可以包含包














