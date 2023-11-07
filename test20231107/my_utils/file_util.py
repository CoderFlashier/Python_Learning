def print_dile_info(file_name):
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except Exception as e:
        return e

    file = f.read()
    print(file)
    print()
    return 0

def append_file_info(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.close()


if __name__ == '__main__':
    ret1 = print_dile_info("E:/Python/Data/20231105/st.txt")
    # append_file_info("E:/Python/Data/20231105/test.txt", "adasdawdasdaw")
    if ret1 != 0:
        print(ret1)
