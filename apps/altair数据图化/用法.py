#!/usr/bin/env python3

import altair as alt

Altair中的基本对象是Chart，它将数据框作为单个参数
#Altair牵牛星  Chart图, (图) 表
chart = alt.Chart(cars)

#Chart有三个基本方法：数据（data）、标记（mark）和编码（encode）
alt.Chart(data).mark_point().encode(
    encoding_1='column_1',
    encoding_2='column_2',
    etc.)
#数据顾名思义，直接导入cars数据集即可。标记和编码则决定着绘制图表的样式
#标记可以让用户在图中以不同形状来表示数据点，比如使用实心点、空心圆、方块等等
#如果我们只调用这个方法，那么所有的数据点都将重叠在一起
#这显然是没有意义的，还需要有编码来指定图像的具体内容。
    x: x轴数值
    y: y轴数值
    color: 标记点颜色
    opacity: 标记点的透明度
    shape: 标记点的形状
    size: 标记点的大小
    row: 按行分列图片
    column: 按列分列图片

#以汽车的耗油量为例，把所有汽车的数据绘制成一个一维散点图，指定x轴为耗油量：
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon'
)
#但是使用mark_point()会让所有标记点混杂在一起，为了让图像更清晰，可以替换成棒状标记点mark_tick()：
alt.Chart(cars).mark_tick().encode(
x='Miles_per_Gallon'
)
#以耗油量为X轴、马力为Y轴，绘制所有汽车的分布，就得到一张二维图像
alt.Chart(cars).mark_line().encode(
x='Miles_per_Gallon',
y='Horsepower'
)
#如果能给不同组的数据分配不同的颜色，就相当于给数据增加了第三个维度。
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon',
y='Horsepower',
color='Origin'
)
#第三个维度“原产国Origin”是一个离散变量。

#使用颜色刻度表，我们还能实现对连续变量的上色，比如在上图中加入“加速度”维度，颜色越深表示加速度越大
alt.Chart(cars).mark_point().encode(
x='Miles_per_Gallon',
y='Horsepower',
color='Acceleration'
)

#相比其他绘图工具，Altair的特点在于不需要调用其他函数，而是直接在数轴上进行修改。
#例如统计不同油耗区间的汽车数量，对X轴使用alt.X()，指定数据和间隔大小，对Y轴使用count()统计数量。
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()'
)

#为了分别表示出不同原产国汽车的油耗分布，前文提到的上色方法也能直方图中使用，这样就构成一幅分段的统计直方图：
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()',
color='Origin'
)

#如果你觉得上图还不够直观，那么可以用column将汽车按不同原产国分列成3张直方图
alt.Chart(cars).mark_bar().encode(
x=alt.X('Miles_per_Gallon', bin=alt.Bin(maxbins=30)),
y='count()',
color='Origin',
column='Origin'
)

#在绘制图片的代码后面，调用interactive()模块，就能实现平移、缩放：


