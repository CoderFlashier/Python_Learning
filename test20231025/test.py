# name = 123
# print("test%d" % name)
# print("test%d" % (2 ** 10))


# name = "zhangsan"
# grade = 10
# growth_rate = 1.2
# growth_day = 7
# print(f"张三{name}，当前成绩{grade}")
# print("增长系数%.2f，%d天过后为%.2f" % (growth_rate, growth_day, (grade*(growth_rate ** 7))))

# name = input("输入：")
# print(name)

# _user_name = input("请输入用户名：")
# greeting = input("请输入问候语：")
# print(f"{_user_name},您好，{greeting}")

# test_bool = 10 > 5
# test_bool2 = 10 < 5
# print(test_bool)
# print(test_bool2)
# print(f"{test_bool2} dasd %s" % test_bool)
# print(f"{test_bool2} dasd %d" % test_bool)

# print(f"abcd == Abcd {"abcd" == "Abcd"}")
# print(f"abcd == abcd {"abcd" == "abcd"}")

# age = int(input("年龄："))# 冒号别忘
# if age >= 18:
#     print(f"你已经{age}了，是成年人了")
# elif age <= 10:
#     print("....")
# else:# 冒号别忘
#     print("好好读书")
# print("123")

# num1 = 10
# if int(input("第一次：")) == num1:
#     print("right")
# elif int(input("第二次：")) == num1:
#     print("right")
# else:
#     print(f"数字是{num1}")

# num = int(input("Hello,enter a number:"))
# if num < 10:
#     if num < 5:
#         print("<5")
#     else:
#         print(">5")
# else:
#     print(">10")

import random
num = random.randint(1, 10)
input1 = int(input("enter a number:"))
if input1 == num:
    print("you are right")
else:
    if input1 > num:
        print("it's too big")
    else:
        print("it's too small")
    input1 = int(input("you have two opportunities:"))
    if input1 == num:
        print("you are right")
    else:
        if input1 > num:
            print("it's too big")
        else:
            print("it's too small")
        input1 = int(input("you have the last one opportunity:"))
        if input1 == num:
            print("you are right")
        else:
            print("you fail")
            print(f"the number is {num}")
