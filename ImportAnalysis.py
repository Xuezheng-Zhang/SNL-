# coding=utf-8
import pandas as pd

# 输入文法分析表文件名 返回rule 
def getAnalysis(filename):
    ana = [[0 for i in range(37)] for j in range(68)]
    df = pd.read_excel(filename)
    df = df.iloc[2:, 2:]

    for i  in range(df.shape[0]):
        for j in range(df.shape[1]):
            if df.iloc[i, j] > 0:
                ana[i + 1][j + 1] = df.iloc[i, j]
    return ana
