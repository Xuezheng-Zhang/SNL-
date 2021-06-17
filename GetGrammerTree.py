# coding=utf-8
from TreeNode import *
from Data import *
from GetTokenList import *

tokenList = getTokenList('词法分析和语法分析/test.txt', '词法分析和语法分析/result.txt')
i = 0 # 当前token下标

def getLineNum(index):
    return tokenList[index][0]
def getSem(index):
    return tokenList[index][1]
def matchSem(index, sem):
    return tokenList[index][1] == sem
def matchNextSem(index, sem):
    return tokenList[index + 1][1] == sem
def matchLex(index, lex):
    return lexType[tokenList[index][2]] == lex
def matchNextLex(index, lex):
    return lexType[tokenList[index + 1][2]] == lex

def Program():
    global i
    root = TreeNode() # 树的根节点
    root.flag = True
    root.nodekind = 'ProK'

    child1 = ProgramHead()
    child2 = DeclarePart()
    child3 = ProgramBody()
    root.child.append(child1)
    root.child.append(child2)
    root.child.append(child3)
    i += 1
    if not matchLex(i, 'DOT'):
        print('end error')

    return root
# 5
def ProgramHead():
    global i
    t = TreeNode()
    t.flag = True
    t.nodekind = 'PheadK'
    t.lineno = getLineNum(i)
    if not matchSem(i, 'program'):
        print('program error')
    i += 1
    if not matchLex(i, 'ID'):
        print('ID error')
    t.name.append(getSem(i))
    return t

def DeclarePart():
    global i
    typeP = TreeNode() # 类型声明
    varP = TreeNode()  # 变量声明
    procP = TreeNode() # 过程声明
    pp = TreeNode() # 声明部分的总结点

    tp1 = TypeDec()
    tp2 = VarDec()
    tp3 = ProcDec()

    if tp1.flag:
        typeP.flag = True
        typeP.nodekind = 'TypeK'
        typeP.lineno = getLineNum(i)
        typeP.child.append(tp1)
    if tp2.flag:
        varP.flag = True
        varP.nodekind = 'VarK'
        varP.lineno = getLineNum(i)
        varP.child.append(tp2)
    if tp3.flag:
        procP = tp3
    if tp2.flag:
        varP.sibling = procP
        if tp1.flag:
            typeP.sibling = varP
            pp = typeP
        else:
            pp = varP
    else:
        if tp1.flag:
            typeP.sibling = procP
            pp = typeP
        else:
            pp = procP
    return pp

def TypeDec():
    global i
    t = TreeNode()
    if matchNextSem(i, 'type'):
        i += 1
        t = TypeDeclaration()
    return t

def TypeDeclaration():
    t = TypeDecList()
    return t

def TypeId(t):
    global i
    if matchLex(i, 'ID'):
        t.name.append(getSem(i))
    else:
        print('ID is expcet')
    return t
# 10
def TypeDef(t):
    global i
    if matchNextSem(i, 'integer') or matchNextSem(i, 'char'):
        i += 1
        BaseType(t)
    elif matchNextSem(i, 'array') or matchNextSem(i, 'record'):
        i += 1
        StructureType(t)
    elif matchNextLex(i, 'ID'):
        i += 1
        t.flag = True
        t.kind = 'DecK'
        t.DecK = 'IdK'
        t.name.append(getSem(i))
    else:
        'found illegal item'
    return t

def BaseType(t):
    global i
    if matchSem(i, 'integer'):
        t.flag = True
        t.kind = 'DecK'
        t.DecK = 'IntegerK'
    elif matchSem(i, 'char'):
        t.flag = True
        t.kind = 'DecK'
        t.DecK = 'CharK'
    return t

def StructureType(t):
    global i
    if matchSem(i, 'array'):
        ArrayType(t)
    elif matchSem(i, 'record'):
        t.flag = True
        t.kind = 'DecK'
        t.DecK = 'RecordK'
        RecType(t)
    return t
# 数组
def ArrayType(t): 
    global i
    i += 1
    if not matchSem(i, '['):
        print('[ is exp')
    i += 1
    if not matchLex(i, 'INTC'):
        print('array low bound must be inst')
    t.flag = True
    t.low = getSem(i)    # 下界
    i += 1
    if not matchLex(i, 'RANGE'):
        print('.. is exp')
    i += 1
    if not matchLex(i, 'INTC'):
        print('array top bound must be inst')
    t.up = getSem(i)     # 上界
    i += 1
    if not matchSem(i, ']'):
        print('] is exp')
    i += 1
    if not matchSem(i, 'of'):
        print('of is exp')
    i += 1
    BaseType(t)
    t.flag = True
    # t.childType = t.name
    t.kind = 'DecK'
    t.DecK = 'ArrayK'
    return t

def RecType(t):
    global i
    i += 1
    p = FieldDecList()
    t.flag = True
    t.child.append(p)
    i += 1
    if not matchSem(i, 'end'):
        print('end is exp')
    return t
# 15
def FieldDecList():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'DecK'
    t.lineno = getLineNum(i)
    p = TreeNode()
    if matchSem(i, 'integer') or matchSem(i, 'char'):
        BaseType(t)
        IdList(t)
        if not matchSem(i, ';'):
            print('; is exp')
        p = FieldDecMore()
    elif matchSem(i, 'array'):
        ArrayType(t)
        IdList(t)
        if not matchSem(i, ';'):
            print('; is exp')
        p = FieldDecMore()
    else:
        print('found unkown item,fielddeclist')
    t.sibling = p
    return t

def FieldDecMore():
    global i
    t = TreeNode()
    if matchNextSem(i, 'end'):
        return t
    elif matchNextSem(i, 'integer') or matchNextSem(i, 'array') or matchNextSem(i, 'char'):
        i += 1
        t.flag = True
        t = FieldDecList()
    else:
        print('unknow item, fielddecmore')
    return t

def IdList(t):
    global i
    i += 1
    if matchLex('ID'):
        t.flag = True
        t.name.append(getSem(i))
    IdMore(t)
    return t

def IdMore(t):
    global i
    if matchNextSem(i, ';'):
        i += 1
    elif matchNextSem(i, ','):
        i += 1
        IdList(t)
    else:
        print('unkown item, idmore')

def TypeDecList():
    global i
    t = TreeNode()
    t.flag = True
    t.lineno = getLineNum(i)
    i += 1
    TypeId(t)
    i += 1
    if not matchSem(i, '='):
        print('= is exp')
    TypeDef(t)
    i += 1
    if not matchSem(i, ';'):
        print('; is exp')
    p = TypeDecMore()
    if p.flag:
        t.sibling = p
    return t

def TypeDecMore():
    global i
    t = TreeNode()
    if matchNextLex(i, 'ID'):
        t = TypeDeclaration()
        return t
    return t

def VarDec():
    global i
    t = TreeNode()
    if matchNextSem(i, 'procedure') or matchNextSem(i, 'begin'):
        return t
    elif matchNextSem(i, 'var'): 
        i += 1
        t = VarDeclaration()
    return t
# 20
def VarDeclaration():
    global i
    t = VarDecList()
    return t

def VarDecList():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'DecK'
    t.lineno = getLineNum(i)
    p = TreeNode()
    TypeDef(t)
    VarIdList(t)
    p = VarDecMore()
    if p.flag:
        t.sibling = p
    return t

def VarDecMore():
    global i
    t = TreeNode()
    if matchNextSem(i, 'procedure') or matchNextSem(i, 'begin'):
        return t
    elif matchNextSem(i, 'integer') or matchNextSem(i, 'char') or matchNextSem(i, 'array') or matchNextSem(i, 'record') or matchNextLex(i, 'ID'):
        t = VarDecList()
    else:
        print('illegal item, vardecmore')
    return t

def VarIdList(t):
    global i
    i += 1
    if matchLex(i, 'ID'):
        t.flag = True
        t.name.append(getSem(i))
    else:
        print('illegal item, varidlist')
    varIdMore(t)

def varIdMore(t):
    global i
    i += 1
    if matchSem(i, ';'):
        return
    elif matchSem(i, ','):
        VarIdList(t)
    else:
        print('illegal item,varidmore')
# 25
#################### 过程声明
def ProcDec():
    global i
    t = TreeNode()
    if matchNextSem(i, 'begin'):
        return t
    elif matchNextSem(i, 'procedure'):
        i += 1
        t = ProcDeclaration()
        p = ProcDec()
        t.flag = True
        t.sibling = p
    else:
        print('illegal, procdec,25')
    return t

def ProcDeclaration():
    global i
    t = TreeNode()
    t.flag = True
    t.nodekind = 'ProcDecK'
    t.lineno = getLineNum(i)
    p1 = TreeNode()
    p2 = TreeNode()
    i += 1
    if not matchLex(i, 'ID'):
        print('id is exp, 26')
    t.name.append(getSem(i))
    i += 1
    if not matchSem(i, '('):
        print('( is exp， 26')
    # 过程参数
    ParamList(t)
    i += 1
    if not matchSem(i, ';'):
        print('; is exp， 26')
    # 过程中的声明
    p1 = ProcDecPart()
    if p1.flag:
        t.child.append(p1)
    # 过程中的语句序列
    p2 = procBody()
    t.child.append(p2)
    return t

def ParamList(t):
    global i
    p = TreeNode()
    if matchNextSem(i, ')'):
        i += 1
        return
    else:
        if matchNextSem(i, 'integer') or matchNextSem(i, 'char') or matchNextSem(i, 'record') or matchNextSem(i, 'array') or matchNextLex(i, 'ID') or matchNextSem(i, 'var'):
            p = ParamDecList()
            t.flag = True
            t.child.append(p)
        else:
            print('illegal, 27')

def ParamDecList():
    global i
    t = Param()
    p = ParamMore()
    t.flag = True
    t.sibling = p
    return t
#!!
def Param():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'DecK'
    t.lineno = getLineNum(i)
    if matchNextSem(i, 'integer') or matchNextSem(i, 'char') or matchNextSem(i, 'record') or matchNextSem(i, 'array') or matchNextLex(i, 'ID'):
        TypeDef(t)
        FormList(t)
    elif matchNextSem(i, 'var'):
        i += 1
        TypeDef(t)
        FormList(t)
    return t
# 30
def FormList(t):
    global i
    i += 1
    if not matchLex(i, 'ID'):
        print('id is exp')
    t.flag = True
    t.name.append(getSem(i))
    i += 1
    FidMore(t)

def FidMore(t):
    global i
    if matchSem(i, ';') or matchSem(i, ')'):
        return
    elif matchSem(i, ','):
        FormList(t)
    else:
        print('illegal,30')

def ParamMore():
    global i
    t = TreeNode()
    if matchSem(i, ')'):
        return t
    elif matchSem(i, ';'):
        t = ParamDecList()
        if t.flag == False:
            print('exp ;')
    return t
################### 过程内部声明
def ProcDecPart():
    global i
    t = DeclarePart()
    return t
################### 过程体
def procBody():
    global i
    t = ProgramBody()
    return t
# 35
def ProgramBody():
    global i
    t = TreeNode()
    t.flag = True
    t.nodekind = 'StmLK'
    t.lineno = getLineNum(i)
    i += 1
    if not matchSem(i, 'begin'):
        print('begin is exp')

    p1 = StmList()
    t.child.append(p1)

    i += 1
    if not matchSem(i, 'end'):
        print('end is exp')
    return t
# 语句序列
def StmList():
    global i
    t = Stm()
    p = StmMore()
    # if t is not None:
    t.flag = True
    t.sibling = p
    return t
# 更多语句
def StmMore():
    global i
    t = TreeNode()
    if matchNextSem(i, ';'): # 有;代表后面还有更多语句
        i += 1
        t = StmList()
    return t
# 单条语句
temp_name = []
def Stm():
    global i
    global temp_name
    t = TreeNode()
    if matchNextSem(i, 'if'):
        i += 1
        t = ConditionalStm()
    elif matchNextSem(i, 'while'):
        i += 1
        t = LoopStm()
    elif matchNextSem(i, 'return'):
        i += 1
        t = ReturnStm()
    elif matchNextSem(i, 'read'):
        i += 1
        t = InputStm()
    elif matchNextSem(i, 'write'):
        i += 1
        t = OutputStm()
    elif matchNextLex(i, 'ID'):
        i += 1
        temp_name.append(getSem(i))
        t = AllCall()
    return t
# !!
def AllCall():
    global i
    t = TreeNode()
    if matchNextLex(i, 'ASSIGN'):
        i += 1
        t = AssignmentRest()
    elif matchNextSem(i, '('):
        i += 1
        t = CallStmRest()
    elif matchNextSem(i, '['):
        i += 1
        t = ArrayRest()
    elif matchNextLex(i, 'POINTER'):
        i += 1
        t = FieldRest()
    return t
# 40
# 数组作为语句的开头
def ArrayRest():
    global i
    global temp_name
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'AssignK'
    t.lineno = getLineNum(i)

    l= TreeNode()
    l.flag = True
    l.kind = 'ExpK'
    l.ExpK = 'ArrayEK'
    l.lineno = getLineNum(i)
    l.name.append(temp_name[0])

    p = Simple_exp()
    l.child.append(p)
    i += 1
    if not matchSem(i, ']'):
        print('] is exp')
    i += 1
    if not matchLex(i, 'ASSIGN'):
        print(':= is exp')
    r = Simple_exp()
    t.child.append(l)
    t.child.append(r)

    return t    
# 赋值语句
def AssignmentRest():
    global i
    global temp_name
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'AssignK'
    t.lineno = getLineNum(i)
    # 左表达式
    p1 = TreeNode()
    p1.flag = True
    p1.kind = 'ExpK'
    p1.ExpK = 'IdEK'
    p1.lineno = getLineNum(i)
    p1.name.append(temp_name[0])
    # 右表达式
    p2 = Simple_exp()
    t.child.append(p1)
    t.child.append(p2)
    return t

def FieldRest():
    global i
    global temp_name
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'AssignK'
    t.lineno = getLineNum(i)

    l= TreeNode()
    l.flag = True
    l.kind = 'ExpK'
    l.ExpK = 'FieldEK'
    l.lineno = getLineNum(i)
    l.name.append(temp_name[0])

    i += 1
    if not matchLex(i, 'ID'):
        print('id is exp')
    p = fieldvar()
    l.child.append(p)
    i += 1
    if not matchLex(i, 'ASSIGN'):
        print(':= is exp')
    r = Simple_exp()
    t.child.append(l)
    t.child.append(r)

    return t
# 函数调用
def CallStmRest():
    global i
    global temp_name
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'CallK'
    t.name.append(getSem(i - 1))

    t.lineno = getLineNum(i)
    p = ActParamList()
    t.child.append(p)
    i += 1
    if not matchSem(i, ')'):
        print(') is exp')
    return t

def ActParamList():
    global i
    t = TreeNode()
    if matchNextSem(i, ')'):
        return t
    elif matchNextLex(i, 'ID') or matchNextSem(i, 'INTC'):
        t = Simple_exp()
        p = ActParamMore()
        t.flag = True
        t.sibling = p
    return t

def ActParamMore():
    global i
    t = TreeNode()
    if matchNextSem(i, ')'):
        return t
    elif matchNextSem(i, ','):
        i += 1
        t = ActParamList()
    return t
# if
def ConditionalStm():
    global i
    t = TreeNode()
    t.flag = True
    t.lineno = getLineNum(i)
    t.kind = 'StmtK'
    t.StmtK = 'IfK'
    # if
    p = Exp()
    t.child.append(p)
    i += 1
    # then
    if not matchSem(i, 'then'):
        print('then is exp')
    p = StmList()
    t.child.append(p)
    # else
    if matchNextSem(i, 'else'):
        i += 1
        p = StmList()
        t.child.append(p)
    i += 1
    if not matchSem(i, 'fi'):
        print('fi is exp')
    return t
# while
def LoopStm():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'WhileK'
    t.lineno = getLineNum(i)
    p1 = Exp()
    t.child.append(p1)
    i += 1
    if not matchSem(i, 'do'):
        print('do is exp')
    p2 = StmList()
    t.child.append(p2)
    i += 1
    if not matchSem(i, 'endwh'):
        print('endwh is exp')
    return t
# read
def InputStm():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'ReadK'
    t.lineno = getLineNum(i)
    i += 1
    if not matchSem(i, '('):
        print('( is exp')
    i += 1
    if not matchLex(i, 'ID'):
        print('id is exp')
    t.name.append(getSem(i))
    i += 1
    if not matchSem(i, ')'):
        print(') is exp')
    return t
# write
def OutputStm():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'WriteK'
    t.lineno = getLineNum(i)
    i += 1
    if not matchSem(i, '('):
        print('( is exp')
    p = Simple_exp()
    t.child.append(p)
    i += 1
    if not matchSem(i, ')'):
        print(') is exp')
    return t
# return
def ReturnStm():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'StmtK'
    t.StmtK = 'ReturnK'
    return t
###################### 处理表达式以及变量
# !!
def Exp():
    global i
    t = TreeNode()
    t = Simple_exp()
    if matchNextSem(i, '<') or matchNextSem(i, '='):
        i += 1
        p1 = TreeNode()
        p1.flag =True
        p1.kind = 'ExpK'
        p1.ExpK = 'OpK'
        p1.name.append(getSem(i))
        p1.lineno = getLineNum(i)
        p1.child.append(t)
        t = p1
        p2 = Simple_exp()
        t.child.append(p2)
    return t
# !!
def Simple_exp():
    global i
    t = term()
    while matchNextSem(i, '+') or matchNextSem(i, '-'):
        i += 1
        p1 = TreeNode()
        p1.flag = True
        p1.lineno = getLineNum(i)
        p1.kind = 'ExpK'
        p1.ExpK = 'OpK'
        p1.name.append(getSem(i))
        p1.child.append(t)
        t = p1
        p2 = term()
        t.child.append(p2)
    return t
# 项的处理
def term():
    global i
    t = factor()
    while matchNextSem(i, '*') or matchNextSem(i, '/'):
        i += 1
        p1 = TreeNode()
        p1.flag = True
        p1.lineno = getLineNum(i)
        p1.kind = 'ExpK'
        p1.ExpK = 'OpK'
        p1.name.append(getSem(i))
        p1.child.append(t)
        t = p1
        p2 = factor()
        t.child.append(p2)
    return t
# !!
def factor():
    global i
    t = TreeNode()
    if matchNextLex(i, 'INTC'):
        i += 1
        t.flag = True
        t.kind = 'ExpK'
        t.ExpK = 'ConstK'
        t.lineno = getLineNum(i)
        t.name.append(getSem(i))
    elif matchNextLex(i, 'ID'):
        i += 1
        t = variable()
    elif matchNextSem(i, '('):
        i += 1
        t = Simple_exp()
        i += 1
        if not matchSem(i, ')'):
            print(') is exp')
    elif matchNextLex(i, 'CHARC'):
        i += 1
        t = TreeNode()
        t.flag = True
        t.kind = 'ExpK'
        t.ExpK = 'CHAREK'
        t.lineno = getLineNum(i)
        t.name.append(getSem(i))
    else:
        print('illegal')
    return t

def variable():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'ExpK'
    t.ExpK = 'IdEK'
    t.lineno = getLineNum(i)
    t.name.append(getSem(i))
    variMore(t)
    return t

def variMore(t):
    global i
    if (matchNextLex(i, 'ASSIGN') or 
        matchNextSem(i ,'*') or
        matchNextSem(i ,'=') or
        matchNextSem(i ,'<') or
        matchNextSem(i ,'+') or
        matchNextSem(i ,'-') or
        matchNextSem(i ,'/') or
        matchNextSem(i ,'else') or
        matchNextSem(i ,')') or
        matchNextSem(i ,';') or
        matchNextSem(i ,',') or
        matchNextSem(i ,'then') or
        matchNextSem(i ,']') or
        matchNextSem(i ,'fi') or
        matchNextSem(i ,'do') or
        matchNextSem(i ,'endwh') or
        matchNextSem(i ,'end')):
        return
    elif matchNextSem(i, '['):
        t.flag = True
        t.ExpK = 'ArrayEK'
        i += 1
        p = Simple_exp()
        t.child.append(p)
        i += 1
        if not matchSem(i, ']'):
            print('] is exp')
    elif matchNextLex(i, 'POINTER'):
        i += 1
        t.flag = True
        t.ExpK = 'FieldEK'
        i += 1
        if not matchLex(i, 'ID'):
            print('id is exp')
        p = fieldvar()
        t.child.append(p)
    else:
        print('illegal')

def fieldvar():
    global i
    t = TreeNode()
    t.flag = True
    t.kind = 'ExpK'
    t.ExpK = 'IdEK'
    t.lineno = getLineNum(i)
    t.name.append(getSem(i))
    fieldvarMore(t)
    return t

def fieldvarMore(t):
    global i
    if (matchNextLex(i, 'ASSIGN') or 
        matchNextSem(i ,'*') or
        matchNextSem(i ,'=') or
        matchNextSem(i ,'<') or
        matchNextSem(i ,'+') or
        matchNextSem(i ,'-') or
        matchNextSem(i ,'/') or
        matchNextSem(i ,')') or
        matchNextSem(i ,';') or
        matchNextSem(i ,',') or
        matchNextSem(i ,'then') or
        matchNextSem(i ,'else') or
        matchNextSem(i ,'fi') or
        matchNextSem(i ,'do') or
        matchNextSem(i ,'endwh') or
        matchNextSem(i ,'end')):
        return
    elif matchNextSem(i, '['):
        i += 1
        t.flag = True
        t.ExpK = 'ArrayEK'
        p = Simple_exp()
        t.child.append(p)
        i += 1
        if not matchSem(i, ']'):
            print('] is exp')

result = open('词法分析和语法分析/result2.txt','w')
def printTree(root, layer):
    global result
    if root is None or root.flag == False: return
    print('   '*layer, end='')
    result.write('\t' * layer)
    # # 行号
    # if root.lineno is not None : 
    #     print(str(root.lineno)+' ', end='')
    #     result.write(str(root.lineno)+'  ')
    # 标志类型
    if root.nodekind is not None:
        print(root.nodekind+'  ', end='')
        result.write(root.nodekind+'  ')
        if root.kind == None and not root.name:   # 确保kind和name空时有换行
            print('')
            result.write('\n')
    # 具体类型
    if root.kind is not None:
        print(str(root.kind)+'  ', end='')
        result.write(root.kind+'  ')
        if root.kind == 'DecK':
            print(str(root.DecK)+'  ', end='')
            result.write(root.DecK+'  ')
        elif root.kind == 'StmtK':
            print(str(root.StmtK)+'  ', end='')
            result.write(root.StmtK+'  ')
        elif root.kind == 'ExpK':
            print(str(root.ExpK)+'  ', end='')  
            result.write(root.ExpK+'  ')
    # 语义信息
    if root.name:
        print(str(root.name))
        result.write(str(root.name)+'\n')

    for son in root.child:
        printTree(son, layer + 1)
    printTree(root.sibling, layer)

# 打印root
root = Program()
printTree(root, 0)