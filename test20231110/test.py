# import pandas as pd
# v1 = [11, 22, 33, 44, 55]
# i = [1, 2, 3, 4, 5]
# sr1 = pd.Series(v1, index=i)
#
# v2 = ["1", "2", '3', '4', '5']
# i = [1, 2, 3, 4, 5]
# sr2 = pd.Series(v2, index=i)
#
# df = pd.DataFrame({"test": sr1, "TEST": sr2})
# print(df)


# import pandas as pd
# df = pd.read_csv("E:/Python/Python深度学习讲义/深度学习系列讲义/深度学习(选学)：Pandas标签库/泰坦尼克.csv", index_col=0)
# age = pd.cut(df['年龄'], [0, 25, 120])
# print(df.pivot_table('是否生还', index=['性别', age], columns="船舱等级"))


# import pandas as pd
# data = pd.read_excel("E:/SZU/活动/泰迪杯/资料/泰迪杯/泰迪杯/2021 泰迪杯数据分析/A题-通讯产品销售和盈利能力分析/非洲通讯产品销售数据.xlsx", sheet_name='SalesData')
# data_date_sort = data.sort_values('日期')
# print(data_date_sort)
#
# data['日期'] = pd.to_datetime(data['日期'], format='%y/%m/%d')
# grouped = data.groupby(data['日期'].dt.year)
# print(grouped)
# data_2017 = grouped.get_group(2017)
# print(data_2017)
# print(data_2017['销售额'].mean())
# data_2017.to_excel("2017.xlsx", index=True)


i = 0
while i>1:
    print("123")

a = 1
while a>1:


