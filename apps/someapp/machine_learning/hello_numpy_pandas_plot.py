#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#20200614, 18:12, pandas plot 出图

#plot data 图表 data
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
#print(data) #1000个数据，序号0-999
data = data.cumsum() #累加之
#print(data) #累加之后的数据集
#data.plot() #plot it, plt.plot(x=, y=)这样的用，但pandas有数据不用再加
#plt.show() #一个折线图

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD')) 
#print(data)
#[1000 rows x 4 columns]
#0-999为一千行序号，ABCD为四列序号
#print(np.random.randn(1000, 4)) #1000行，4列

data = data.cumsum() #累加之
#print(data) #1000rows * 4cloumns

#data.plot()
#plt.show() #四根折线，ABCD为颜色，0-999为X轴，数据内容为Y轴

#plot methods:
#bar, hist, box, kde, area, scatter, hexbin, 很多，还可调线宽细等等
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1') #scatter一般只有两个数据x,y，
data.plot.scatter(x='A', y='C', label='Class 2', ax=ax) #一张图打印两组scatter数据
#plt.show() #深蓝色数据一组class，另一个默认的蓝色的class，散点图，X轴为A的， Y轴为BC，都是-25+40之间描点



#20200614, 16:50, pandas介绍#############################
exit(0)

s = pd.Series([1, 3, 6, np.nan, 44, 1])
#print(s)
#0     1.0
#1     3.0
#2     6.0
#3     NaN
#4    44.0
#5     1.0
#dtype: float64

dates = pd.date_range('20160101', periods = 6)
#print(dates)
#DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               #'2016-01-05', '2016-01-06'],
              #dtype='datetime64[ns]', freq='D')

#指定索引，行的index和列的columns，变成这样的指定的名称
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
#print(df)
                   #a         b         c         d
#2016-01-01  1.707561 -0.909484  0.257639  0.704688
#2016-01-02  0.554242  1.923956  0.535173  0.336753
#2016-01-03  0.093186  0.539803  2.676914  0.603193
#2016-01-04  1.610692  0.392151 -1.624620 -0.189798
#2016-01-05  0.455815 -1.771078 -0.079618 -0.392536
#2016-01-06  0.596082 -2.152981  0.383541  0.819679

#默认的，没有指定其名称（数据骨架/框架，嗯，支个架子）
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
#print(df1)
   #0  1   2   3
#0  0  1   2   3
#1  4  5   6   7
#2  8  9  10  11

#从字典生成数据框架
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
#print(df2) #为了对齐数据，就把只有一行的，直接复制成另一行的数据
     #A          B    C  D      E    F
#0  1.0 2013-01-02  1.0  3   test  foo
#1  1.0 2013-01-02  1.0  3  train  foo
#2  1.0 2013-01-02  1.0  3   test  foo
#3  1.0 2013-01-02  1.0  3  train  foo

#print(df2.dtypes)
#A           float64
#B    datetime64[ns]
#C           float32
#D             int32
#E          category
#F            object
#dtype: object

#print(df2.index)
#Int64Index([0, 1, 2, 3], dtype='int64')

#print(df2.columns)
#Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')



#20200614, 16:46, numpy array 分割###################

A = np.arange(12).reshape((3, 4))
#print(A)
#[[ 0  1  2  3]
 #[ 4  5  6  7]
 #[ 8  9 10 11]]

#算了，不这样学了。
#用时学。就是，应用中，哪个不懂，查哪个
#不过基本概念还是得有，至少，得知道不懂的是哪个，有的查


#20200613, 20:52, numpy array 合并####################
exit(0)

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

#垂直合并
C = np.vstack((A, B)) #vertical stack
#[[1 1 1]
 #[2 2 2]]
#print(A.shape, C.shape)
#(3,) (2, 3) #C有两行三列，二维的矩阵

#水平合并
D = np.hstack((A, B)) #horizontal stack
#print(D)
#[1 1 1 2 2 2]
#print(D.shape)
#(6,) #还是一维的

#一维不能扭转。这不是矩阵
#print(A.T)
#[1 1 1]

E = A[np.newaxis, :] #为A加个维度，原来是一行，现在是1行3列的
#[[1 1 1]]
#print(E.shape)
#(1, 3)

F = A[:, np.newaxis] #为A加个维度，原来是一行，现在是3行1列
#print(F)
#[[1]
 #[1]
 #[1]]

#串连
#G = np.concatenate((A, B, B, A))
#print(G)
#[1 1 1 2 2 2 2 2 2 1 1 1]
A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

G = np.concatenate((A, B, B, A), axis=0) #要求列合并
#print(G)
#[[1]
 #[1]
 #[1]
 #[2]
 #[2]
 #[2]
 #[2]
 #[2]
 #[2]
 #[1]
 #[1]
 #[1]]

G = np.concatenate((A, B, B, A), axis=1) #要求行合并
#print(G)
#[[1 2 2 1]
 #[1 2 2 1]
 #[1 2 2 1]]


#20200613, 20:42, numpy索引############################
exit(0)

A = np.arange(3, 15)
#print(A)
#[ 3  4  5  6  7  8  9 10 11 12 13 14]

#print(A[3]) #6

A = np.arange(3, 15).reshape((3, 4)) #row:3, column:4
#print(A)
#[[ 3  4  5  6]
 #[ 7  8  9 10]
 #[11 12 13 14]]
#print(A[2]) #索引行数
#[11 12 13 14]
#print(A[1][1]) #8, 第1行 第1列
#print(A[2][1]) #12, 
#print(A[2, 1]) #12, 和上面的一样，表示第2行，第1列
#print(A[2, :]) #[11 12 13 14], 第2行的所有数
#print(A[:, 1]) #[ 4  8 12], 第1列的所有数
#print(A[1, 1:2]) #[8], 第1行，第2个数
#print(A[1, 1:3]) #[8 9], 第1行，第2至3个数

#遍历行
#for row in A:
    #print(row)
#[3 4 5 6]
#[ 7  8  9 10]
#[11 12 13 14]

#遍历列，即，把原有的矩阵翻转下再遍历。把列变成行即可
#for column in A.T:
    #print(column)
#[ 3  7 11]
#[ 4  8 12]
#[ 5  9 13]
#[ 6 10 14]

#print(A.flatten()) #拉平他
#[ 3  4  5  6  7  8  9 10 11 12 13 14]

#逐个遍历。把矩阵拉平了再遍历～～～
#for item in A.flat:
    #print(item)


#20200613, 18:42, numpy基础运算2######################################
exit(0)

A = np.arange(2, 14).reshape((3, 4))
#print(A)
#[[ 2  3  4  5]
 #[ 6  7  8  9]
 #[10 11 12 13]]

#print(np.argmin(A)) #0，最小值的索引
#print(np.argmax(A)) #11, 最大值的索引
#print(np.mean(A)) #7.5， 平均值
#print(A.mean()) #7.5, 平均值，和上面的一样
#print(np.average(A)) #7.5, 平均值， 和上面一样
#print(np.median(A)) #7.5, 中位数，因为是均等数列

#print(np.cumsum(A)) #累积加上去
#[ 2  5  9 14 20 27 35 44 54 65 77 90]

#print(np.diff(A)) #累差，每两个数的差，会少一列
#[[1 1 1]
 #[1 1 1]
 #[1 1 1]]

#print(np.nonzero(A)) #输出非0的行数，列数，两组数据，因为都是非0的，00，至33,都是非0
#(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))

#print(np.sort(A)) #逐行排序。因为已经有序，所以是一样的。
#[[ 2  3  4  5]
 #[ 6  7  8  9]
 #[10 11 12 13]]

#print(np.transpose(A)) #矩阵的翻转，行成列，列成行
#print(A.T)
#[[ 2  6 10]
 #[ 3  7 11]
 #[ 4  8 12]
 #[ 5  9 13]]
#print((A.T).dot(A)) #翻转再和原来的矩阵乘法
#[[140 158 176 194]
 #[158 179 200 221]
 #[176 200 224 248]
 #[194 221 248 275]]

#print(np.clip(A, 5, 9)) #只保留5-9,小于5的变成5, 大于9的变成9
#[[5 5 5 5]
 #[6 7 8 9]
 #[9 9 9 9]]

#print(np.mean(A, axis=0)) #所有的这样的计算可以指定对行或对列计算，0为列1为行
#[ 6.  7.  8.  9.]
#print(np.mean(A, axis=1)) #axis为1,对行进行计算，共3行
#[  3.5   7.5  11.5]


#20200613, 18:42, numpy基础运算#######################################
exit(0)

a = np.array([10, 20, 30, 40])
#print(a)
#[10 20 30 40]

b = np.arange(4)
#print(b)
#[0 1 2 3]

c = a - b
#print(c)
#[10 19 28 37]

c = a + b
#print(c)
#[10 21 32 43]

c = a * b
#print(c)
#[  0  20  60 120]

c = b**2
#print(c)
#[0 1 4 9]

c = 10*np.sin(a)
#print(c)
#[-5.44021111  9.12945251 -9.88031624  7.4511316 ]

#print(b<3)
#[ True  True  True False]
#print(b==3)
#[ True  True  True False]

a = np.array([[1, 1],
                [0, 1]])
b = np.arange(4).reshape((2, 2))
#print(a)
#[[1 1]
 #[0 1]]
#print(b)
#[[0 1]
 #[2 3]]

#逐个相乘
c = a * b
#逐个与相应列相乘，矩阵运算结果
#第一个矩阵的列数（column）和第二个矩阵的行数（row）相同
#C=AB=[[a11b11 + a12b21 + a13b31, a11b12 + a12b22 + a13b32] 
        #A的第一行逐个乘B的第一列之和， A的第一行逐个乘B的第二列之和（即A的行的列数与B的列的行数相同
        #[a21b11 + a22b21 + a23b31, a21b12 + a22b22 + a23b32]
        #A的第二行逐个乘B的第一列之和， A的第二行逐个乘B的第二列之和
c_dot = np.dot(a, b)
#print(c)
#[[0 1]
 #[0 3]]
#print(c_dot)
#[[2 4] #1*0+1*2, 1*1+1*3
 #[2 3]] #0*0+1*2, 0*1+1*3

c_dot_2 = a.dot(b) #same with np.dot
#print(c_dot_2)
#[[2 4]
 #[2 3]]

a = np.random.random((2,4)) #row2, column4
#print(a)
#[[ 0.66849452  0.13524115  0.14279931  0.97064921]
 #[ 0.68329126  0.88740019  0.87110137  0.78473165]]

#print(np.sum(a))
#5.14370865131
#print(np.min(a))
#0.135241150186
#print(np.max(a))
#0.970649206879

#print(a)
#[[ 0.57436564  0.68861354  0.43965899  0.0153792 ]
 #[ 0.64015302  0.99805981  0.850247    0.86196397]]
#print(np.sum(a, axis=1)) #按行求和
#[ 1.71801737  3.35042379]
#print(np.min(a, axis=0)) #按列求最小值
#[ 0.57436564  0.68861354  0.43965899  0.0153792 ]
#print(np.max(a, axis=1)) #按行求最大值
#[ 0.68861354  0.99805981]



#20200613, 13:35, 创建array##########################
exit(0)

a = np.array([2, 23, 4], dtype=np.float)
print(a.dtype)

a = np.zeros((3, 4))
print(a)

a = np.ones((3, 4), dtype=np.int)
print(a)

a = np.empty((3, 4))
print(a)

#创造连续数组，10-19的数据，2步长
a = np.arange(10, 20, 2)
print(a)
#[10 12 14 16 18]

a = np.arange(12)
print(a)
#[ 0  1  2  3  4  5  6  7  8  9 10 11]

a = np.arange(12).reshape((3,4))
print(a)
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

# 开始端1，结束端10，且分割成20个数据，生成线段
a = np.linspace(1, 10, 20)
print(a)
#[  1.           1.47368421   1.94736842   2.42105263   2.89473684
#   3.36842105   3.84210526   4.31578947   4.78947368   5.26315789
#   5.73684211   6.21052632   6.68421053   7.15789474   7.63157895
#   8.10526316   8.57894737   9.05263158   9.52631579  10.        ]

a = np.linspace(1, 10, 20).reshape((5,4))
print(a)
#[[  1.           1.47368421   1.94736842   2.42105263]
 #[  2.89473684   3.36842105   3.84210526   4.31578947]
 #[  4.78947368   5.26315789   5.73684211   6.21052632]
 #[  6.68421053   7.15789474   7.63157895   8.10526316]
 #[  8.57894737   9.05263158   9.52631579  10.        ]]


#20200613, 13:24, numpy属性################################
exit(0) 

array = np.array([[1, 2, 3], 
            [2, 3, 4]])

print(array)

print('number of dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)


