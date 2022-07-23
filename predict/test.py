import numpy as np
from numpy import *

def load_matrix(path):
    A = zeros((1992, 1), dtype=float)

    f = open(path)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    A_row = 0  # 表示矩阵的行，从0行开始
    for line in lines:  # 把lines中的数据逐行读取出来
        list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        A[A_row, :] = list[0:3]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1  # 然后方阵A的下一行接着读
        # print(line)
    return A

data1 = load_matrix("score/predictions0.txt")
data2 = load_matrix("score/predictions00.txt")
data3 = load_matrix("score/predictions000.txt")
data4 = load_matrix("score/predictions0000.txt")
data5 = load_matrix("score/predictions00000.txt")
data = zeros((1992,1), dtype=float)

for i in range(len(data1)):
    data[i] = (data1[i] + data2[i] + data3[i] + data4[i] + data5[i]) / 5
    # data[i] = round(a[0], 6)

data = np.mean(data,axis=1,dtype=float)
np.savetxt("score/Avgprediction.txt", data)

