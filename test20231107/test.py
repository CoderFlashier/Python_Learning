# 基本捕获语法
# try:
#     f = open("E:/Python/Data/20231107/test.txt", "r", encoding="UTF-8")
#     # 此时文件是不存在的，即无法以r模式打开文件
# except:
#     f = open("E:/Python/Data/20231107/test.txt", "w", encoding="UTF-8")
#     # 出现异常时，except起作用


# try:
#     print(name)
#     # name 未定义，必报错
# except (NameError, ZeroDivisionError) as e:
#     # 当出现NameError时，执行下面的语句
#     print("error")
#     print(e)
#     # 输出异常信息


# def func1():
#     print("func1 start")
#     num1 = 1 / 0
#     # 出现异常：0为分母
#
# def func2():
#     print("func2 start")
#     func1()
#     # 异常传递到func2
#
# def func3():
#     print("func3 start")
#     try:
#         func2()
#         # 异常传递到func3
#         # 这里如果不捕获异常，则整个程序会报错
#     except Exception as e:
#         print("error")
#         print(e)
#
# func3()


# from my_package.my_mode2 import test
# ret = test(1, 2)
# print(ret)


# def func1():
#     num1 = 1 / 0
# try:
#     func1()
# except ZeroDivisionError as a:
#     print("error")


# import time
# time.sleep(5)


# from my_utils import file_util
# from my_utils import str_util


import json
data = [{"a": "adasda你好", "b": "dadasdaddaed"}, {"c": "dadsa dadada", "d": "dadadwdasda"}]
data_str = json.dumps(data, ensure_ascii=False)
# 传入ensure_ascii=False，表示不使用unicode表示中文（不传的话一般用unicode表示中文）（不传中文可以不写）（如果为True，中文会转换为unicode）
# 将数据转换为json
print(type(data_str))
# str类型
print(data_str)
data_list = json.loads(data_str)
# 将数据转换回列表
print(type(data_list))
print(data_list)