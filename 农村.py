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
list_data1 = sheet.col_values(9)[1:]
list_data2 = sheet.col_values(10)[1:]


x_data=list_data
y_data=list_data1
z_data=list_data2


from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

x_data = ["{:.0f}年".format(i) for i in x_data[1:]]
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis(
        y_data[0],
       y_data[1:],
        yaxis_index=0,
        color="#5793f3",    #稍微修改下颜色
        z=0
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name=z_data[0],
            # min_=0,
            # max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            # axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name=y_data[0],    #我们删除了降水保留了蒸发，这里改为蒸发量
            # min_=0,
            # max_=250,
            position="right",
            offset=0,    #这里是Y轴间距，由80改为0即两个Y轴重合，当然我们已经删除了原来的一个Y轴，所以相当于把第二Y轴左移
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            # axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        title_opts=opts.TitleOpts(title=rows[9]),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)


line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        z_data[0],
        z_data[1:],
        yaxis_index=1,    #删了一个Y轴，Y轴索引由2改为1
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line)
grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="10%", pos_right="40%"), is_control_axis_index=True)
grid.render('农村.html')
