# coding=utf-8
from Data import *

tokenList = []  # Token 序列
temp = [] # 用来保存未处理完的字符
need = False
def getWord(line, i , state, level, flag):
    global temp
    global need
    while i < len(line):
        if need: state = 's5'
        if state == 's0':
            temp.append(line[i])
            if line[i] in  Letter:
                state = 's1'
            elif line[i] in Number:
                state = 's2'
            elif line[i] in single and line[i] != '.' and line[i] != ':':
                state = 's3'
            elif line[i] == ':':
                state = 's4'
            elif line[i] == '{':
                state = 's5'
                need = True
            elif line[i] == '.':
                state = 's6'
                if i == len(line) - 1: # . 是最后一个符号
                    tokenList.append([level, '.', findLexId('.', 's6')])
                    temp.clear()
            elif line[i] == "'":
                state = 's7'
            elif line[i] in ' \t\n':
                temp.clear()
                pass
            else:
                state = 's8'
        elif state == 's1':
            # 如果当前读入的仍然是字符或者数字则加入temp
            if line[i] in Letter or line[i] in Number and i != len(line) - 1:
                temp.append(line[i])
            else:
                #检查是否是保留字
                if ''.join(temp) in reservedWord:
                    tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's1_1')])
                else:
                    tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's1_2')])
                i -= 1
                state = 's0' # 恢复到开始状态
                temp.clear() # 清空
        elif state == 's2':
            if line[i] in Number:
                temp.append(line[i])
            else:
                tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's2')])
                i -= 1
                state = 's0' # 恢复到开始状态
                temp.clear() # 清空
        elif state == 's3':
            tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's3')])
            i -= 1
            state = 's0'
            temp.clear()
        elif state == 's4':
            temp.append(line[i])
            if ''.join(temp) == ':=':
                tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's4')])
            else:
                print(temp)
                tokenList.append([level, ':', findLexId(':', 's4')])
                i -= 1
            state = 's0'
            temp.clear()
        elif state == 's5':
            if line[i] == '}':
                need = False
                state = 's0'
                temp.clear()
        elif state == 's6':
            temp.append(line[i])
            if ''.join(temp) == '..':
                tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's6')])
            else:
                tokenList.append([level, '.', findLexId('.', 's6')])
                i -= 1
            state = 's0'
            temp.clear()    
        elif state == 's7':
            if line[i] in Letter or line[i] in Number:
                temp.append(line[i])
            elif line[i] == "'":
                tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's7')])
                state = 's0'
                temp.clear()
            else:
                temp.append(line[i])
                tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's7')])
                state = 's8'
                temp.clear()
        elif state == 's8':
            tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's8')])
            i -= 1
            state = 's0'
            temp.clear()
        
        if i == len(line) - 1 and temp and flag:   # 当最后一行全部分析完后 temp还剩了字符
            tokenList.append([level, ''.join(temp), findLexId(''.join(temp), 's9')])
        i += 1

# 函数生成一个Token 序列   
def getTokenList(inPut, outPut):
    lines = open(inPut,'r').readlines()
    lineNum = 0 # 当前行号初始化为1
    for line in lines: # 逐行扫描
        lineNum += 1
        if lineNum == len(lines):
            flag = True  # flag == True 代表当前是最后一行
        else:
            flag = False   
        getWord(line, 0, 's0', lineNum, flag)
    tokenList.append([len(lines), 'EOF', findLexId('EOF', 's10')])
    # 输出到文件中
    output = open(outPut, 'w')
    for token in tokenList:
        if lexType[token[2]] == 'RESERVEDWORD':
            output.write("行号:"+str(token[0])+"  "+token[1]+"   类型:"+token[1].upper()+"\n")
            print(token[0], " ", token[1], " ",token[1].upper())
        else:
            output.write("行号:"+str(token[0])+"  "+token[1]+"   类型:"+lexType[token[2]]+"\n")
            print(token[0], " ", token[1], " ",lexType[token[2]])
    output.close()
    return tokenList
