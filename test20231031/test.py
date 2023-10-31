# str1 = "wdnmd"
#
# count = 0
# for i in str1:
#     count += 1
#
# print(count)


# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(count)
#
# str1 = "wndausbfv"
# str2 = "awndiuahbsnf"
#
# my_len(str1)
# my_len(str2)


# def hello():
#     print("welcome to python")
#     print("good luck")
#
# hello()


# def add(x,y):
#     """
#     一个加法程序
#     :param x: 第一个数
#     :param y: 第二个数
#     :return: 返回两数相加的值
#     """
#     result = x + y
#     return result
#
# x = int(input())
# y = int(input())
# ret = add(x, y)
# print(ret)


# def tem(x):
#     if x > 37.5:
#         print("leave")
#     else:
#         print("welcome")
#
# temperature = int(input("please enter a number:"))
# tem(temperature)


# def printf():
#     print("2")
#     return None
#
# print(type(printf()))


# num = 10
# def test():
#     global num
#     num = 200
#     # 注意这里用global修饰num和num的赋值需要分开写
#     print(num)
#
# def print1():
#     print(num)
#
# test()
# print1()

"""
以下是一段利用自定义函数和循环简单模拟的ATM程序，要点如下：
1、设计一个开始菜单，用于显示进行各项操作的选项，供用户选择
2、利用自定义函数分别实现存款、取款、查询和退出功能
3、在完成一个操作后，回到主菜单，进行下一次操作的选择
"""
# money = 50000
# # 定义初始余额
#
#
# def welcome():
#     # 显示菜单
#     print(f"please enter a number to chose what you want to do.")
#     print("1.Deposit\t2.Withdraw money")
#     print("3.Query\t\t0.Exit")
#     # 1、存款 2、取款 3、查询 4、退出
#     # 一个制表符不能对齐，可以用两个
#
#
# def deposit():
#     global money
#     # 将局部变量转换为全局变量
#     # 这里的全局变量声明要在使用这个变量之前
#     print(f"Now,you have {money} dollars.")
#     in1 = int(input("Enter a number:"))
#     print(f"There are {money + in1} dollars in your card.")
#     money += in1
#
#
# def query():
#     print(f"Now,you have {money} dollars.")
#
#
# def withdraw_money():
#     global money
#     print(f"Now,you have {money} dollars.")
#     out1 = int(input("Enter a number:"))
#     if out1 <= money:
#         # 判断余额是否充足
#         print(f"You will get {out1} dollars and there are {money - out1} dollars in your card.")
#         money -= out1
#     else:
#         print("Error")


"""
以下是一段利用自定义函数和循环简单模拟的ATM程序，要点如下：
1、设计一个开始菜单，用于显示进行各项操作的选项，供用户选择
2、利用自定义函数分别实现存款、取款、查询和退出功能
3、在完成一个操作后，回到主菜单，进行下一次操作的选择
"""
# money = 50000
# # 定义初始余额
#
#
# def welcome():
#     # 显示菜单
#     print(f"please enter a number to chose what you want to do.")
#     print("1.Deposit\t2.Withdraw money")
#     print("3.Query\t\t0.Exit")
#     # 1、存款 2、取款 3、查询 4、退出
#     # 一个制表符不能对齐，可以用两个
#
#
# def deposit():
#     global money
#     # 将局部变量转换为全局变量
#     # 这里的全局变量声明要在使用这个变量之前
#     print(f"Now,you have {money} dollars.")
#     in1 = int(input("Enter a number:"))
#     print(f"There are {money + in1} dollars in your card.")
#     money += in1
#
#
# def query():
#     print(f"Now,you have {money} dollars.")
#
#
# def withdraw_money():
#     global money
#     print(f"Now,you have {money} dollars.")
#     out1 = int(input("Enter a number:"))
#     if out1 <= money:
#         # 判断余额是否充足
#         print(f"You will get {out1} dollars and there are {money - out1} dollars in your card.")
#         money -= out1
#     else:
#         print("Error")
#
#
# name = input("Enter your name:")
# # 输入用户姓名
# print(f"Welcome {name}.")
# welcome()
# choose = int(input())
# # 第一次选择
#
# while choose:
#     # 直接用chose作为判断依据，当chose为0时，退出循环
#     if choose == 1:
#         deposit()
#         welcome()
#         choose = int(input())
#         # 在每一次操作后重新选择操作
#     elif choose == 2:
#         withdraw_money()
#         welcome()
#         choose = int(input())
#     elif choose == 3:
#         query()
#         welcome()
#         choose = int(input())
#     else:
#         print("Error")
#         welcome()
#         choose = int(input())
#
# print("Exit")
# name = input("Enter your name:")
# # 输入用户姓名
# print(f"Welcome {name}.")
# welcome()
# choose = int(input())
# # 第一次选择
#
# while choose:
#     # 直接用chose作为判断依据，当chose为0时，退出循环
#     if choose == 1:
#         deposit()
#         welcome()
#         choose = int(input())
#         # 在每一次操作后重新选择操作
#     elif choose == 2:
#         withdraw_money()
#         welcome()
#         choose = int(input())
#     elif choose == 3:
#         query()
#         welcome()
#         choose = int(input())
#     else:
#         print("Error")
#         welcome()
#         choose = int(input())
#
# print("Exit")


# def add(x, y):
#     return x + y
#
#
# a = int(input())
# b = int(input())
# ret = add(a, b)
# print(ret)


# def test():
#     global num
#     num = 100
#
# test()
# print(num)


my_list =[['123', 321], ["1234567", False]]
# 列表的嵌套
# 这个列表要有两个元素，每个元素都是列表
print(my_list)
print(type(my_list))