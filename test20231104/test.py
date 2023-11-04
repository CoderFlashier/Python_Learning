# list1 = ["abc", "cba", "abc", "abcbca", "123456", 123456]
# set1 = set()
# # 注意这要用set(),不能直接放一个{}
# for a in list1:
#     set1.add(a)
#
# print(set1)


# dict1 = {"a": "awjmdasmk", "b":65411, "c":41, "d":"awdasd"}
# for a in dict1.keys():
#     print(dict1[a])


# dict1 = {"a": {"info1": "A", "info2": 3000, "info3": "1"},
#          "b": {"info1": "B", "info2": 5000, "info3": "2"},
#          "c": {"info1": "B", "info2": 7000, "info3": "3"},
#          "d": {"info1": "A", "info2": 4000, "info3": "1"},
#          "e": {"info1": "B", "info2": 6000, "info3": "2"}}
# # 字典的嵌套
# for key in dict1:
#     # 逐个取出元素进行判断
#     if dict1[key]["info3"] == "1":
#         dict1[key]["info3"] = "2"
#         dict1[key]["info2"] += 1000
#
# print(dict1)


# dict1 = {"a":"dasd", "b":"ajsbduiaw", "c":"dadasd"}
# list1 = list(dict1)
# print(list1)


# n = int(input())
# a = 1
# list1 = []
# while a <= n:
#     list1.append(a)
#     a += 1
#
# list2 = []
# for b in list1:
#     if b % 6 == 0:
#         list2.append(b)
#
# print(list1)
# print(list2)

# import random
# class_list = [[], [], []]
# teacher = {"A", "B", "C", "D", "E", "F", "G"}
# for teacher in teacher:
#     num = random.randint(0,2)
#     print(num)
#     class_list[num].append(teacher)
#
# print(class_list)


# my_list = [1321, 11651, 319813, 9845, 4897, 464, 194, 984, 131, 6513, 44313]
# new_list = my_list[2:8:2]
# print(new_list)
# print(type(new_list))

# list1 = ["abc", "cba", "abc", "abcbca", "123456", 123456]
# set1 = set()
# # 注意这要用set(),不能直接放一个{}
# for a in list1:
#     set1.add(a)
#
# print(set1)


# def test():
#     return 1, [123, 131], "132"
#
# x, y, z = test()
# print(x)
# print(y)
# print(z)


# def info(name, age, sex):
#     print(f"{name},{age},{sex}")
#
# info("zhangsan", sex = "male", age = 23)


def info(name, age, sex = "male"):
    print(f"{name},{age},{sex}")

info("zhangsan", age = 23, sex = "female")