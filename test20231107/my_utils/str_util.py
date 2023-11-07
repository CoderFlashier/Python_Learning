def str_reverse(str1):
    str2 = str1[::-1]
    return str2


def substr(str1, x, y, z):
    substr1 = str1[x: y: z]
    return substr1


if __name__ == '__main__':
    ret1 = str_reverse("adoiuhauifhgaukfhqaukfhaf")
    ret2 = substr("aduhasuihduqad", 2, 20, 2)
    print(ret1)
    print(ret2)