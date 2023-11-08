# # 导入Line功能
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# # 导入工具
#
# # 得到折线图对象
# line = Line()
# # 添加X轴数据
# line.add_xaxis(["China", "American", "Britain"])
# # 添加Y轴数据
# line.add_yaxis("GDP",[2, 1, 3])
# # 生成图表
# line.set_global_opts(
#     title_opts=TitleOpts(title="test", pos_left="center", pos_bottom="1%"),
#     # 设置标题,pos设置位置,最后记得加逗号
#     legend_opts=LegendOpts(is_show=True),
#     # 控制图例是否展示
#     toolbox_opts=ToolboxOpts(is_show=True),
#     # 工具箱是否展示
#     visualmap_opts=VisualMapOpts(is_show=True)
#     # 视觉映射
# )
# # 关键字传参
#
# line.render()
# # 会出现一个html文件

#
# import json
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
# # 处理数据
# f_us = open("E:/Python/黑马程序员资料/资料/第1-12章资料/资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
# us_data = f_us.read()
# us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# # 把不规范的数据替换成空字符串，相当于删掉
# us_data = us_data.strip(");")
# # 去掉最后的
# # JSON转换为python字典
# us_dict = json.loads(us_data)
# # 获取trend key
# us_trend_data = us_dict['data'][0]['trend']
# #  取出两份数据
# # 日期数据(取到314，即2020年）
# us_x_data = us_trend_data['updateDate'][:314:]
# # 取具体数据
# us_y_data = us_trend_data['list'][0]['data'][:314:]
#
#
# f_jp = open("E:/Python/黑马程序员资料/资料/第1-12章资料/资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
# jp_data = f_jp.read()
# jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# jp_data = jp_data.strip(");")
# jp_dict = json.loads(jp_data)
# jp_trend_data = jp_dict['data'][0]['trend']
# jp_x_data = jp_trend_data['updateDate'][:314:]
# jp_y_data = jp_trend_data['list'][0]['data'][:314:]
#
#
# f_in = open("E:/Python/黑马程序员资料/资料/第1-12章资料/资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
# in_data = f_in.read()
# in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# in_data = in_data.strip(");")
# in_dict = json.loads(in_data)
# in_trend_data = in_dict['data'][0]['trend']
# in_x_data = in_trend_data['updateDate'][:314:]
# in_y_data = in_trend_data['list'][0]['data'][:314:]
#
# # 生成图表
# line = Line()
# # 构建折线图对象
# line.add_xaxis(us_x_data)
# # x轴是共用的，使用一个国家即可
# line.add_yaxis("American", us_y_data, label_opts=LabelOpts(is_show=False))
# # 系列设置,这里设置不显示数据
# line.add_yaxis("Japan", jp_y_data, label_opts=LabelOpts(is_show=False))
# line.add_yaxis("India", in_y_data, label_opts=LabelOpts(is_show=False))
# # y轴不共用，单独添加
#
# # 全局配置
# line.set_global_opts(
#     title_opts=TitleOpts(title="test", pos_left="center", pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True)
#     )
#
# # 调用render
# line.render()
#
# f_in.close()
# f_jp.close()
# f_us.close()


# from pyecharts.charts import Map
# # 准备地图对象
# map = Map()
# # 准备数据
# data = [
#     ("北京市", 1),
#     ("上海市", 2),
#     ("广东省", 3)
# ]
#
# map.add("test", data, "china")
# # 名称、数据、地图类型（默认中国）
# map.render()


# import json
# from pyecharts.charts import Map
# from pyecharts.options import *
# f = open("E:/Python/黑马程序员资料/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
# data = f.read()
# f.close()
# data_dict = json.loads(data)
# data_list = []
# province_data_list = data_dict['areaTree'][0]["children"][3]['children']
# for province_data in province_data_list:
#     province_name = province_data['name'] + '市'
#     province_data = province_data['total']['confirm']
#     data_list.append((province_name, province_data))
#
#
# map = Map()
# map.add("test", data_list, "河南")
# map.set_global_opts(
#     title_opts=TitleOpts(title="test"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 99, "lable": "1~99", "color": "#CCFFFF"},
#             {"min": 100, "max": 999, "lable": "100~999", "color": "#FFFF99"},
#             {"min": 1000, "max": 4999, "lable": "1000~4999", "color": "#FF9966"},
#             {"min": 5000, "max": 9999, "lable": "5000~9999", "color": "#FF6666"},
#             {"min": 10000, "max": 99999, "lable": "10000~99999", "color": "#CC3333"},
#             {"min": 100000,"lable": ">=100000", "color":"#990033"}
#         ]
#     )
# )
# map.render("test.html")


# from pyecharts.charts import Bar
# from pyecharts.options import LabelOpts
# bar = Bar()
# bar.add_xaxis(["China", "American", "England"])
# bar.add_yaxis("test", [2, 1, 3], label_opts=LabelOpts(position="right"))
# # 把数字标签移到右边
# bar.reversal_axis()
# # 反转x和y轴
# bar.render("test1.html")


# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import LabelOpts
# from pyecharts.globals import ThemeType
# bar1 = Bar()
# bar1.add_xaxis(["China", "American", "England"])
# bar1.add_yaxis("test", [2, 1, 3], label_opts=LabelOpts(position="right"))
# bar1.reversal_axis()
#
# bar2 = Bar()
# bar2.add_xaxis(["China", "American", "England"])
# bar2.add_yaxis("test", [2, 1, 3], label_opts=LabelOpts(position="right"))
# bar2.reversal_axis()
#
# bar3 = Bar()
# bar3.add_xaxis(["China", "American", "England"])
# bar3.add_yaxis("test", [2, 1, 3], label_opts=LabelOpts(position="right"))
# bar3.reversal_axis()
#
# timeline = Timeline(
#     {"theme": ThemeType.PURPLE_PASSION}
# )
# timeline.add(bar1, "1")
# timeline.add(bar2, "2")
# timeline.add(bar3, "3")
# # 此时需要用时间线绘图，而不是bar对象绘图
# timeline.add_schema(
#     play_interval=1000,
#     # 自动播放间隔（毫秒）
#     is_timeline_show=True,
#     # 是否在播放时显示时间线
#     is_auto_play=True,
#     # 是否自动播放
#     is_loop_play=True
#     # 是否循环自动播放
# )
# timeline.render("basic timeline.html")


# my_list = [["a", 30], ["b", 40], ["c", 50]]
#
# my_list.sort(key=lambda element:element[1], reverse=False)
# print(my_list)



from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
f = open("E:/Python/黑马程序员资料/资料/第1-12章资料/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# 这个文件的编码为ANSI，即根据系统语言确定，默认中文为GB2312
data_lines = f.readlines()
f.close()
data_lines.pop(0)
# 删掉第一行无用数据
# 先定义一个字典对象
data_dict = {}
timeline = Timeline({"theme": ThemeType.LIGHT})
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 防止以科学计数法显示数字
    try:
        data_dict[year].append([country, gdp])
        # 当key不存在时，调用会报错
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

sorted_year_list = sorted(data_dict.keys())
# 字典无序，先给key排序
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 按gdp排序
    year_data = data_dict[year][:8:]
    # 取前八的数据
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)
        # y轴添加gdp

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    # 反转顺序
    bar.add_xaxis(x_data)
    bar.add_yaxis("gdp(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("1960-2019全球GDP前8国家.html")