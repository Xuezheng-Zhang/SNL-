# coding=utf-8
########################
# Token种类
lexType = [
	# 保留字
	'PROGRAM', 'PROCEDURE', 'TYPE', 'VAR', 'IF',
	'THEN', 'ELSE', 'FI', 'WHILE', 'DO',
	'ENDWH', 'BEGIN', 'END', 'READ', 'WRITE',
	'ARRAY', 'OF', 'RECORD', 'RETURN', 'INTEGER', 'CHAR',
    # 多字符单词符号
    'ID',        # 标识符 s1
	'INTC',      # 整形常量 s2
	'CHARC',     # 字符串 s7
    # 特殊符号
    'PLUS' , 'MINUS', 'TIMES', 'OVER', # + - * /
    'LPAREN', 'RPAREN',  # ( )
    'DOT',       # .
    'LMIDPAREN', 'RMIDPAREN', # [ ]
    'SEMI',      # ;
    'COLON',     # :
    'COMMA',     # ,
    'LT',        # <
    'EQ',        # =     
	'ASSIGN',    # :=
	'UNDERANGE', #  ..
    # 薄记单词符号
	'ENDFILE',   # EOF			
	'ERROR',      # 错误

    'RESERVEDWORD', # 保留字
    'OP', # 运算符
    'RANGE', # 数组下标
    'POINTER'
    ]

# 保留字
reservedWord = [ 'program', 'procedure', 'type', 'var', 'if',
                 'then', 'else', 'fi', 'while', 'do',
                 'endwh', 'begin', 'end', 'read', 'write',
                 'array', 'of', 'record', 'return', 'integer', 'char']
# 单分界符 
single = [',', ';', '+', '-', '*', '/', '<', '=', 
          '(', ')', '[', ']', '.', ':', 'EOF']
# 双分界符
single = ['..', ':=']
# 字母
Letter = ''.join([chr(i) for i in range(97, 123)])
Letter += Letter.upper()
# 整形常量
Number = '0123456789'

# token -> lextype中序号
def findLexId(word, state):
    if state == 's1_1':      # 保留字
        return lexType.index('RESERVEDWORD')
    elif state == 's1_2':    # 标识符
        return lexType.index('ID')
    elif state == 's2':      # 整形常量
        return lexType.index('INTC')
    elif state == 's7':      # 字符串
        return lexType.index('CHARC')
    elif word == '+': return lexType.index('OP')
    elif word == '-': return lexType.index('OP')
    elif word == '*': return lexType.index('OP')
    elif word == '/': return lexType.index('OP')
    elif word == '(': return lexType.index('LPAREN')
    elif word == ')': return lexType.index('RPAREN')
    elif word == '.': return lexType.index('DOT')
    elif word == '[': return lexType.index('LMIDPAREN')
    elif word == ']': return lexType.index('RMIDPAREN')
    elif word == ';': return lexType.index('SEMI')
    elif word == ':': return lexType.index('COLON')
    elif word == ',': return lexType.index('COMMA')
    elif word == '<': return lexType.index('LT')
    elif word == '=': return lexType.index('EQ')
    elif word == ':=': return lexType.index('ASSIGN')
    elif word == '..': return lexType.index('RANGE')
    elif word == 'EOF': return lexType.index('ENDFILE')
    else: return lexType.index('ERROR')

#########################
#终极符
# terminal = ['null', 'program', 'type', 'integer', 'char', 'array',
#                     'INTC', 'record', 'end', 'var', 'procedure',
#                     'begin', 'if', 'then', 'else', 'fi',
#                     'while', 'do', 'endwh', 'read', 'write',
#                     'return', 'ID', '.', ';', ',',
#                     '(', ')', '[', ']', '<', 
#                     '=', '+', '-', '*', '/',
#                     ':=']

# #非终极符
# nonTerminal = ['null',  'Program', 'ProgramHead', 'ProgramName', 'DeclarePart', 'TypeDecpart',
#                         'TypeDec', 'TypeDecList', 'TypeDecMore', 'TypeId', 'TypeDef',
#                         'BaseType', 'StructureType', 'ArrayType', 'Low', 'Top',
#                         'RecType', 'FieldDecList', 'FieldDecMore', 'IdList', 'IdMore',
#                         'VarDecpart', 'VarDec', 'VarDecList', 'VarDecMore', 'VarIdList',
#                         'VarIdMore', 'ProcDecpart', 'ProcDec', 'ProcDecMore', 'ProcName',
#                         'ParamList', 'ParamDecList', 'ParamMore', 'Param', 'FormList',
#                         'FidMore', 'ProcDecPart', 'ProcBody', 'ProgramBody', 'StmList',
#                         'StmMore', 'Stm', 'AssCall', 'AssignmentRest', 'ConditionalStm',
#                         'LoopStm', 'InputStm', 'Invar', 'OutputStm', 'ReturnStm',
#                         'CallStmRest', 'ActParamList', 'ActParamMore', 'RelExp', 'OtherRelE',
#                         'Exp', 'OtherTerm', 'Term', 'OtherFactor', 'Factor',
#                         'Varialbe', 'VariMore', 'FieldVar', 'FiledVarMore', 'CmpOp',
#                         'AddOp', 'MulOp']

# #LL1 分析表
# analysis = getAnalysis('/Users/zhangxuezheng/Desktop/python/词法分析和语法分析/SNL语言文法的LL（1）分析表.xls')

# #SNL上下文无关文法
# rule = [] # rule存共104条文法
# class Rule:  #定义文法结构 A + Blist
#     def __init__(self):
#         self.A = ''
#         self.B = []

# r = Rule()
# r.A = "SNL"
# r.B.append(".")
# rule.append(r)

# r = Rule()
# r.A = "Program"
# r.B.append("ProgramHead")
# r.B.append("DeclarePart")
# r.B.append("ProgramBody")
# r.B.append(".")
# rule.append(r)

# r = Rule()
# r.A = "ProgramHead"
# r.B.append("program")
# r.B.append("ProgramName")
# rule.append(r)

# r = Rule()
# r.A = "ProgramName"
# r.B.append("ID")
# rule.append(r)

# r = Rule()
# r.A = "DeclarePart"
# r.B.append("TypeDecpart")
# r.B.append("VarDecpart")
# r.B.append("ProcDecpart")
# rule.append(r)

# r = Rule()
# r.A = "TypeDecpart"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "TypeDecpart"
# r.B.append("TypeDec")
# rule.append(r)

# r = Rule()
# r.A = "TypeDec"
# r.B.append("type")
# r.B.append("TypeDecList")
# rule.append(r)

# r = Rule()
# r.A = "TypeDecList"
# r.B.append("TypeId")
# r.B.append("=")
# r.B.append("TypeDef")
# r.B.append(";")
# r.B.append("TypeDecMore")
# rule.append(r)

# r = Rule()
# r.A = "TypeDecMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "TypeDecMore"
# r.B.append("TypeDecList")
# rule.append(r)

# r = Rule()
# r.A = "TypeId"
# r.B.append("ID")
# rule.append(r)

# r = Rule()
# r.A = "TypeDef"
# r.B.append("BaseType")
# rule.append(r)

# r = Rule()
# r.A = "TypeDef"
# r.B.append("StructureType")
# rule.append(r)

# r = Rule()
# r.A = "TypeDef"
# r.B.append("ID")
# rule.append(r)

# r = Rule()
# r.A = "BaseType"
# r.B.append("integer")
# rule.append(r)

# r = Rule()
# r.A = "BaseType"
# r.B.append("char")
# rule.append(r)

# r = Rule()
# r.A = "StructureType"
# r.B.append("ArrayType")
# rule.append(r)

# r = Rule()
# r.A = "StructureType"
# r.B.append("RecType")
# rule.append(r)

# r = Rule()
# r.A = "ArrayType"
# r.B.append("array")
# r.B.append("[")
# r.B.append("Low")
# r.B.append("..")
# r.B.append("Top")
# r.B.append("]")
# r.B.append("of")
# r.B.append("BaseType")
# rule.append(r)

# r = Rule()
# r.A = "Low"
# r.B.append("INTC")
# rule.append(r)

# r = Rule()
# r.A = "Top"
# r.B.append("INTC")
# rule.append(r)

# r = Rule()
# r.A = "RecType"
# r.B.append("record")
# r.B.append("FieldDecList")
# r.B.append("end")
# rule.append(r)

# r = Rule()
# r.A = "FieldDecList"
# r.B.append("BaseType")
# r.B.append("IdList")
# r.B.append(";")
# r.B.append("FieldDecMore")
# rule.append(r)

# r = Rule()
# r.A = "FieldDecList"
# r.B.append("ArrayType")
# r.B.append("IdList")
# r.B.append(";")
# r.B.append("FieldDecMore")
# rule.append(r)

# r = Rule()
# r.A = "FieldDecMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "FieldDecMore"
# r.B.append("FieldDecList")
# rule.append(r)

# r = Rule()
# r.A = "IdList"
# r.B.append("ID")
# r.B.append("IdMore")
# rule.append(r)

# r = Rule()
# r.A = "IdMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "IdMore"
# r.B.append(",")
# r.B.append("IdList")
# rule.append(r)

# r = Rule()
# r.A = "VarDecpart"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "VarDecpart"
# r.B.append("VarDec")
# rule.append(r)

# r = Rule()
# r.A = "VarDec"
# r.B.append("var")
# r.B.append("VarDecList")
# rule.append(r)

# r = Rule()
# r.A = "VarDecList"
# r.B.append("TypeDef")
# r.B.append("VarIdList")
# r.B.append(";")
# r.B.append("VarDecMore")
# rule.append(r)

# r = Rule()
# r.A = "VarDecMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "VarDecMore"
# r.B.append("VarDecList")
# rule.append(r)

# r = Rule()
# r.A = "VarIdList"
# r.B.append("ID")
# r.B.append("VarIdMore")
# rule.append(r)

# r = Rule()
# r.A = "VarIdMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "VarIdMore"
# r.B.append(",")
# r.B.append("VarIdList")
# rule.append(r)

# r = Rule()
# r.A = "ProcDecpart"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ProcDecpart"
# r.B.append("ProcDec")
# rule.append(r)

# r = Rule()
# r.A = "ProcDec"
# r.B.append("procedure")
# r.B.append("ProcName")
# r.B.append("(")
# r.B.append("ParamList")
# r.B.append(")")
# r.B.append(";")
# r.B.append("ProcDecPart")
# r.B.append("ProcBody")
# r.B.append("ProcDecMore")
# rule.append(r)

# r = Rule()
# r.A = "ProcDecMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ProcDecMore"
# r.B.append("ProcDec")
# rule.append(r)

# r = Rule()
# r.A = "ProcName"
# r.B.append("ID")
# rule.append(r)

# r = Rule()
# r.A = "ParamList"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ParamList"
# r.B.append("ParamDecList")
# rule.append(r)

# r = Rule()
# r.A = "ParamDecList"
# r.B.append("Param")
# r.B.append("ParamMore")
# rule.append(r)

# r = Rule()
# r.A = "ParamMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ParamMore"
# r.B.append(";")
# r.B.append("ParamDecList")
# rule.append(r)

# r = Rule()
# r.A = "Param"
# r.B.append("TypeDef")
# r.B.append("FormList")
# rule.append(r)

# r = Rule()
# r.A = "Param"
# r.B.append("var")
# r.B.append("TypeDef")
# r.B.append("FormList")
# rule.append(r)

# r = Rule()
# r.A = "FormList"
# r.B.append("ID")
# r.B.append("FidMore")
# rule.append(r)

# r = Rule()
# r.A = "FidMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "FidMore"
# r.B.append(",")
# r.B.append("FormList")
# rule.append(r)

# r = Rule()
# r.A = "ProcDecPart"
# r.B.append("DeclarePart")
# rule.append(r)

# r = Rule()
# r.A = "ProcBody"
# r.B.append("ProgramBody")
# rule.append(r)

# r = Rule()
# r.A = "ProgramBody"
# r.B.append("begin")
# r.B.append("StmList")
# r.B.append("end")
# rule.append(r)

# r = Rule()
# r.A = "StmList"
# r.B.append("Stm")
# r.B.append("StmMore")
# rule.append(r)

# r = Rule()
# r.A = "StmMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "StmMore"
# r.B.append(";")
# r.B.append("StmList")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("ConditionalStm")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("LoopStm")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("InputStm")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("OutputStm")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("ReturnStm")
# rule.append(r)

# r = Rule()
# r.A = "Stm"
# r.B.append("ID")
# r.B.append("AssCall")
# rule.append(r)

# r = Rule()
# r.A = "AssCall"
# r.B.append("AssignmentRest")
# rule.append(r)

# r = Rule()
# r.A = "AssCall"
# r.B.append("CallStmRest")
# rule.append(r)

# r = Rule()
# r.A = "AssignmentRest"
# r.B.append("VariMore")
# r.B.append(":=")
# r.B.append("Exp")
# rule.append(r)

# r = Rule()
# r.A = "ConditionalStm"
# r.B.append("if")
# r.B.append("RelExp")
# r.B.append("then")
# r.B.append("StmList")
# r.B.append("else")
# r.B.append("StmList")
# r.B.append("fi")
# rule.append(r)

# r = Rule()
# r.A = "LoopStm"
# r.B.append("while")
# r.B.append("RelExp")
# r.B.append("do")
# r.B.append("StmList")
# r.B.append("endwh")
# rule.append(r)

# r = Rule()
# r.A = "InputStm"
# r.B.append("read")
# r.B.append("(")
# r.B.append("Invar")
# r.B.append(")")
# rule.append(r)

# r = Rule()
# r.A = "Invar"
# r.B.append("ID")
# rule.append(r)

# r = Rule()
# r.A = "OutputStm"
# r.B.append("write")
# r.B.append("(")
# r.B.append("Exp")
# r.B.append(")")
# rule.append(r)

# r = Rule()
# r.A = "ReturnStm"
# r.B.append("return")
# r.B.append("(")
# r.B.append("Exp")
# r.B.append(")")
# rule.append(r)

# r = Rule()
# r.A = "CallStmRest"
# r.B.append("(")
# r.B.append("ActParamList")
# r.B.append(")")
# rule.append(r)

# r = Rule()
# r.A = "ActParamList"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ActParamList"
# r.B.append("Exp")
# r.B.append("ActParamMore")
# rule.append(r)

# r = Rule()
# r.A = "ActParamMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "ActParamMore"
# r.B.append(",")
# r.B.append("ActParamList")
# rule.append(r)

# r = Rule()
# r.A = "RelExp"
# r.B.append("Exp")
# r.B.append("OtherRelE")
# rule.append(r)

# r = Rule()
# r.A = "OtherRelE"
# r.B.append("CmpOp")
# r.B.append("Exp")
# rule.append(r)

# r = Rule()
# r.A = "Exp"
# r.B.append("Term")
# r.B.append("OtherTerm")
# rule.append(r)

# r = Rule()
# r.A = "OtherTerm"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "OtherTerm"
# r.B.append("AddOp")
# r.B.append("Exp")
# rule.append(r)

# r = Rule()
# r.A = "Term"
# r.B.append("Factor")
# r.B.append("OtherFactor")
# rule.append(r)

# r = Rule()
# r.A = "OtherFactor"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "OtherFactor"
# r.B.append("MulOp")
# r.B.append("Term")
# rule.append(r)

# r = Rule()
# r.A = "Factor"
# r.B.append("(")
# r.B.append("Exp")
# r.B.append(")")
# rule.append(r)

# r = Rule()
# r.A = "Factor"
# r.B.append("INTC")
# rule.append(r)

# r = Rule()
# r.A = "Factor"
# r.B.append("Variable")
# rule.append(r)

# r = Rule()
# r.A = "Variable"
# r.B.append("ID")
# r.B.append("VariMore")
# rule.append(r)

# r = Rule()
# r.A = "VariMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "VariMore"
# r.B.append("[")
# r.B.append("Exp")
# r.B.append("]")
# rule.append(r)

# r = Rule()
# r.A = "VariMore"
# r.B.append(".")
# r.B.append("FieldVar")
# rule.append(r)

# r = Rule()
# r.A = "FieldVar"
# r.B.append("ID")
# r.B.append("FieldVarMore")
# rule.append(r)

# r = Rule()
# r.A = "FieldVarMore"
# r.B.append("null")
# rule.append(r)

# r = Rule()
# r.A = "FieldVarMore"
# r.B.append("[")
# r.B.append("Exp")
# r.B.append("]")
# rule.append(r)

# r = Rule()
# r.A = "CmpOp"
# r.B.append("<")
# rule.append(r)

# r = Rule()
# r.A = "CmpOp"
# r.B.append("=")
# rule.append(r)

# r = Rule()
# r.A = "AddOp"
# r.B.append("+")
# rule.append(r)

# r = Rule()
# r.A = "AddOp"
# r.B.append("-")
# rule.append(r)

# r = Rule()
# r.A = "MulOp"
# r.B.append("*")
# rule.append(r)

# r = Rule()
# r.A = "MulOp"
# r.B.append("/")
# rule.append(r)
