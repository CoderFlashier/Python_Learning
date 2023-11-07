def test(a, b):
    return a + b

if __name__ == '__main__':
    # __name__ 是一个内置变量，当程序运行是，__name__会被命名为__main__
    # 而当mode被导入是，__name__则不会被命名为__main__
    test(1, 2)