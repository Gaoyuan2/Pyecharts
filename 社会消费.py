import numpy as np
import xlrd

# 打开文件
from pyecharts.charts import Bar, Pie, Line, Grid

workbook = xlrd.open_workbook('彭水社会经济情况.xls')

# 获取所有sheet
sheet_name = workbook.sheet_names()[0]

# 根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(0) # sheet索引从0开始

# 获取整行和整列的值（数组）
rows = sheet.row_values(0) # 获取第一行内容
cols = sheet.col_values(0) # 获取第一列内容

# 获取单元格内容
cell_A1 = sheet.cell(0,0).value
cell_A2 = sheet.cell_value(1,0)
cell_B1 = sheet.row(0)[1].value

# 获取第一列数据到列表中
list_data = sheet.col_values(0)[1:]
list_data1 = sheet.col_values(5)[1:]
list_data2 = sheet.col_values(6)[1:]

x_data=list_data
y_data=list_data1
z_data=list_data2


from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

x_data = ["{:.0f}年".format(i) for i in x_data[1:]]

# 创建图表
line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name=z_data[0],
        y_axis=z_data[1:],
        symbol="circle",
        is_smooth=True,
        is_symbol_show=True,
    )
    .set_global_opts(title_opts=opts.TitleOpts(title=rows[5]))
)

line.render('社会消费.html')

