# coding=utf-8
class TreeNode:
    def __init__(self):
        self.child = []      # 存储子节点
        self.sibling = None  # 下一个兄弟节点
        self.lineno = None   # 程序行号
        self.nodekind = None # 语法树节点类型
        self.kind = None     # 语法树节点具体类型
        self.DecK = None     # kind == DecK
        self.StmtK = None    # kind == StmtK
        self.ExpK = None     # kind == ExpK
        self.idnum = None    # 标识符个数
        self.name = []     # 标识符名字 idname  
        self.typename = None # 类型名 
        # 数组
        self.low = None # 下界
        self.up = None  # 上界 
        self.childType = None # 数组成员类型
        # 函数（过程）
        self.paramt = None   # 函数（过程）参数类型
        self.flag = False    # 标志对象是否被赋过值