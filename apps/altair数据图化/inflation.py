#!/usr/bin/env python3
#完成这个之后，集成到网页中，把数据集用文本存储读取，不对，直接对象存储读取
#费事巴啦的还得搞这那，最后生成数据还得存储下来，这直接在这里面搞就行了。人生啊

import altair as alt
import pandas as pd

#100块钱最后会膨胀会多少？其实银行定期不对，应该更高点，但先这样算着
x_list = []
y_list = []
x = 1
y = 100

for i in range(40):
    y = y*1.055
    x = i+1
    x_list.append(x)
    y_list.append(y)

#print(x_list, y_list)

#exit(0)

#准备要用的datas,X轴和Y轴对应数据
datas = pd.DataFrame({'x':x_list, 'y':y_list})


chart = alt.Chart(datas).mark_line().encode(
x = 'x', #这个是之前pandas数据里面的字典名
y = 'y'
)


chart.serve()



