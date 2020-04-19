
from .Value import Value
from .Variable import Input,Output
from functools import reduce
from .Root      import Root





def assign(opl:Value,opr:Value):
    tmp = opl
    tmp += opr

def smart_assign(op1:Value,op2:Value,outer=False):
    if isinstance(op1,Input) and isinstance(op2,Output):
        if outer:
            tmp = op1
            tmp += op2
        else:
            tmp = op2
            tmp += op1
    elif isinstance(op1,Output) and isinstance (op2,Input):
        if outer:
            tmp = op2
            tmp += op1
        else:
            tmp = op1
            tmp += op2
    else:
        raise Exception()

def LCA(*node_list):
    tree_list = [x.ancestors() for x in node_list]
    common_path = list(reduce(lambda x,y:set(x)&set(y),tree_list))
    return None if not common_path else common_path[0]

def linkable(op1,op2):
    if isinstance(op1,Input) and not isinstance(op2,Input):
        return True
    elif isinstance(op2,Input) and not isinstance(op1,Input):
        return True
    else:
        return False

