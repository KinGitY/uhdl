#import traceback
#from abc import abstractmethod
from .BasicFunction import join_name



class Root(object):


    def __init__(self):
        super().__init__()
        #super(Root,self).__init__()
        self._name        = None
        self._father      = None
        self._father_type = None               #保留father type为空，子类不修改father_type就会出错

    def set_name(self,name:str):
        object.__setattr__(self,'_name',name)

    def set_father(self,father):
        object.__setattr__(self,'_father',father)
    
    def set_father_type(self,*T):
        ''' 这个方法设置了本对象应当指向的father对象的类型,默认的father对象的类型为None'''
        self._father_type = T

    @property
    def name(self) -> str:
        return self._name

    @property
    def father(self):
        return self._father
    


    def __setattr__(self,name,value):
        if isinstance(value,Root):
            #print(name,'  ',value)
            value.set_name(name)
            value.set_father(self)
            #print(value.name)
        object.__setattr__(self,name,value)

    #=============================================================================================
    # father get
    #=============================================================================================

    def father_until(self,T):
        if isinstance(self,T):
            return self
        elif self.father is None:
            return self
        else:
            return self.father.father_until(T)

    def father_until_not(self,T):
        if not isinstance(self,T):
            return self
        elif self.father is None:
            return self
        else:
            return self.father.father_until_not(T)        

    #=============================================================================================
    # name get
    #=============================================================================================

    # def join_name(self,*args):
    #     args_without_none = [x for x in args if x is not None]
    #     return '_'.join(args_without_none)

    def full_name(self):
        if self.father is None:
            return ''
        else:
            return join_name(self.father.full_name,self.name)


    def name_until(self,T):
        if isinstance(T,type):
            if isinstance(self,T):
                return self.name
            elif self.father is None:
                return ''
            else:
                return join_name(self.father.name_until(T),self.name)
        else:
            if self is T:
                return self.name
            elif self.father is None:
                return ''
            else:
                return join_name(self.father.name_until(T),self.name)

    def name_before(self,T):
        if isinstance(T,type):
            if isinstance(self.father,T):
                return self.name
            elif self.father is None:
                return ''
            else:
                return join_name(self.father.name_before(T),self.name)
        else:
            if self.father is T:
                return self.name
            elif self.father is None:
                return ''
            else:
                return join_name(self.father.name_before(T),self.name)


    def name_until_not(self,T):
        if not isinstance(self,T):
            return self.name
        elif self.father is None:
            return self.name
        else:
            return join_name(self.father.name_until_not(T),self.name)

    def name_before_not(self,T):
        if self.father is None:
            return self.name
        elif not isinstance(self.father,T):
            return self.name
        else:
            return join_name(self.father.name_before_not(T),self.name)


    def ancestors_core(self):
        return [self] + self._father.ancestors_core() if self._father is not None else [self]


    def ancestors(self,until=None,before=None,has_self=False,error=True):
        full_ancestors = self.ancestors_core()

        if until != None and before != None:
            raise Exception()
        elif until != None:
            if until in full_ancestors:
                result = full_ancestors[:full_ancestors.index(until)+1]
            elif not error:
                result = full_ancestors
            elif until not in full_ancestors:
                raise Exception()
        elif before != None:
            if before in full_ancestors:
                result = full_ancestors[:full_ancestors.index(before)]
            elif not error:
                result = full_ancestors
            elif before not in full_ancestors:
                raise Exception()

        else:
            result = full_ancestors

        if not has_self:
            result.remove(self)
        return result

    def get_circuit(self,name:str):
        return get_circuit(self,name)

    def set_circuit(self,name:str,value):
        return set_circuit(self,name,value)

    get = get_circuit
    set = set_circuit


def get_circuit(obj:Root,name:str):
    return getattr(obj,name)

def set_circuit(obj:Root,name:str,value:Root) -> Root:
    setattr(obj,name,value)
    return value



    # @father.setter
    # def father(self,father):
    #     ''' 获取father的时候应当检查father的类型是否正确，对于Root而言
    #         father必须是Root类型'''
    #     if not isinstance(father,self._father_type):
    #         raise TypeError("The father set is a %s,expect a %s." %(type(father),self._father_type))
    #     self._father = father
    # @abstractmethod






        #print(self.father,self.name)
        #print(T)
        #print(isinstance(self,T))

        
    #def __get_name(self):
    #    pass

    #def __not_define(self):
    #    raise Exception

    #@property
    #def full_name(self):
    #    return self.name_join(self.get_father_full_name(),self.name)
#
#
#
    #def name_join(self,*args):
    #    return '_'.join(args)


