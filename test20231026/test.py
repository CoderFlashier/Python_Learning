# i = 0
# num = 1
# sum = 0
# while i < 100:
#     print(num)
#     i += 1
#     sum += num
#     num += 1
#
# print(sum)


# import random
# num = random.randint(1,100)
# # 生成一个1~100的随机数
# count = 0
# # 用于记录猜数的次数
# mark = True
# while mark:
#     # 这里直接用mark，不需要判断是否为1
#     input_num = int(input("enter a number:"))
#     if input_num == num:
#         count += 1
#         mark = False
#         # 当猜中时，将mark改为False，跳出循环
#         print("you are right")
#     else:
#         count += 1
#         if input_num > num:
#             print("it's too big")
#         else:
#             print("it's too small")
#
# print(f"game over,you have tried {count} times")


# print("hell0", end = ' ')
# print("world", end = '')

# print("hello\tworld")
# print("hell\tword")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         if j == i:
#             print(f"{i}*{j}={i * j}\t")
#             # 通过制表符 \t 实现对齐，当为最后一个式子时换行
#             # 换行也可以通过 print() 实现
#         else:
#             print(f"{i}*{j}={i * j}\t", end='')
#             # 除了最后一个式子以外不换行，用end=空字符串实现
#         j += 1
#     i += 1


# string = "Hello World"
# for i in string:
#     print(i)
# # 以一列的形式输出Hello World


# i = 0
# count = 0
# string = "Hello World addo abnsbnkhjvfbabkjbfhbabfa,msjfg"
# for x in string:
#     if x == 'a':
#         count += 1
# print(f"the number of a is {count}")


# for i in range(20, 100, 4):
#     print(i)
#     # 输出从24开始间隔4的数字，不含100


# for i in range(10):
#     for j in range(20, 100, 6):
#         print(j)


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i}*{j}={i * j}\t", end='')
#     print()
#     # 实现换行


money = 10000
for i in range(1, 21):
    import random
    grade = random.randint(1, 10)
    if grade >= 5:
        print(f"第{i}号{grade}分，发")
        money -= 1000
    else:
        print(f"第{i}号{grade}分，下一个")
        continue
    if money == 0:
        break
print("结束")
