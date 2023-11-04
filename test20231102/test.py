# my_list = ["abc",123,3210]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[-3])
# print(my_list[-2])
# print(my_list[-1])
#
# my_list = [["abc", 123], [3210]]
# print(my_list[0])
# print(my_list[0][1])


# my_list = ["abc", 123, 3210]
# my_list2 = ["efg", 456, 3210]
# my_list.extend(my_list2)
# print(my_list)


# my_list = ["abc", 123, 3210]
# my_list2 = ["efg", 456, 3210]
# del my_list[1]
# ret = my_list2.pop(1)
# # pop有返回值，为移除（取出）的内容
# print(my_list)
# print(my_list2)
# print(ret)


# my_list = ["abc", 123, 3210, "abc", 123, 3210]
# my_list.remove(123)
# # 如果要删掉两个的话要用两次
# print(my_list)
# my_list.clear()
# print(my_list)


# my_list = ["abc", 123, 3210, "abc", 123, 3210]
# count = my_list.count(123)
# print(count)
# count2 = len(my_list)
# print(count2)


# my_list = [21, 25, 21, 23, 23, 22, 10]
# my_list.append(31)
# my_list.extend([29, 33, 30])
# num1 = my_list[0]
# count = len(my_list)
# num2 = my_list[count - 1]
# mark = my_list.index(31)
# print(num1)
# print(num2)
# print(mark)
# print(my_list)

# # 利用遍历分别取出奇数和偶数
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = []
# list2 = []
# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#        list1.append(my_list[index])
#     index += 1
#
# for num in my_list:
#     if num % 2 == 1:
#         list2.append(num)
#
# print(list1)
# print(list2)


# t1 = ()
# print(type(t1))


# t1 = (1, 2, 3, [45612, "wdakjnsf", "dwa000"])
# t1[3][2] = "abc"
# print(t1)


str1 = "123 654 7893121"
my_str = str1.count("13")
print(my_str)
