# def test(func):
#     ret = func(1, 2)
#     print(ret)
#
#
# test(lambda x, y: x + y)


# def test(func):
#     ret = func(1, 2)
#     print(ret)
#
#
# def add(x, y):
#     return x + y
#
#
# test(add)
# # 输出3



# def test(*args):
#     print(args)
#
# test(215613, "abcd", 468413, "awdjaoshf", [4654, "awdasd"])


# def test(**kwargs):
#     print(kwargs)
#
# test(a=123, b="abcd", c=["adhas", 13213])


# f = open("E:/Python/Data/test.txt", "r", encoding="UTF-8")
# # 打开文件
# print(type(f))
# a = f.read(2)
# print(a)
# # 读取文件
#
# line1 = f.readline()
# # 读取一行数据
# # 会受到上一个读取操作的影响
# print(type(line1))
# print(line1)
#
# list1 = f.readlines()
# # 逐行读取并转换为列表
# # 会受到上一个读取操作的影响
# print(type(list1))
# print(list1)

# import time
# f = open("E:/Python/Data/test.txt", "r", encoding="UTF-8")
# for line in f:
#     print(line)
# f.close()
# time.sleep(2000)
# # 用sleep模拟占用情况


# import time
# with open("E:/Python/Data/test.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(line)
# time.sleep(1000)
# # 此时虽然程序还在运行，但是打开的文件已经关闭


# count = 0
# f = open("E:/Python/Data/20231105/word.txt")
# for line in f:
#     count += line.count("itheima")
# f.close()
# print(count)

# import time
# f = open("E:/Python/Data/20231105/test2.txt", "w", encoding="UTF-8")
# # python可以识别\/但是同时只能用一种，不能混用
# f.write("Hello,world!")
# # time.sleep(2000)
# # 创建并写入文件，此时只是写入内存，因此如果此时程序未结束，在文件管理器中打开文件会发现文件是空白的
# f.flush()
# # 将内存中的内容写入硬盘
# # time.sleep(2000)
# f.close()
# # close其实内置了flush的功能


# f = open("E:/Python/Data/20231105/test3.txt", "a", encoding="UTF-8")
# f.write("hello")
# f.close()
#
# f = open("E:/Python/Data/20231105/test3.txt", "w", encoding="UTF-8")
# line1 = f.read()
# print(line1)
# f.close()


f1 = open("E:/Python/Data/20231105/bill.txt", "r", encoding="UTF-8")
f2 = open("E:/Python/Data/20231105/bill.txt.bak", "a", encoding="UTF-8")
for line in f1:
    if line.count("测试") == 1:
        continue
    else:
        f2.write(line)
f1.close()
f2.close()
