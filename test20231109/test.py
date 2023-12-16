# class Student:
#     name = None
#     sex = None
#     nationality = None
#     native_place = None
#     age = None
#
#
# stu1 = Student()
# stu1.name = "zhangsan"
# stu1.sex = "male"
# stu1.nationality = "China"
# stu1.native_place = "GuangDong"
# stu1.age = 18


# class Test:
#     test_data = None
#     def test(self, str1):
#         print(f"abc,{str1},{self.test_data}")
#
# test1 = Test()
# test1.test_data = "abcd"
# test1.test("abc")


# class Student:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#
# stu1 = Student(name="zhangsan", sex="male", age=18)
# print(stu1.name, end=' ')
# print(stu1.sex, end=' ')
# print(stu1.age)


# class Student:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def __str__(self):
#         return f"student: name:{self.name}, age:{self.age}, address:{self.address}"
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     def __op(self):
#         return "A"
#
# stu1 = Student("a", 15, "abc")
# stu2 = Student("b", 17, "abd")
# print(stu1 <= stu2)


# class Phone:
#     __is_5g_enable = True
#
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g")
#         else:
#             print("4g")
#
#     def call_by_5g(self):
#         self.__check_5g()
#
#
# p1 = Phone()
# p1.call_by_5g()


import random
num1 = random.randint(20, 50)