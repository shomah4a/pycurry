#-*- coding:utf-8 -*-

import inspect
import types


def getFunc(func):

    if isinstance(func, types.MethodType):
        if func.im_self is not None:
            return func.im_func, (func.im_self,)
        return func.im_func, ()

    return func, ()
  


def getDefaultArgs(spec):

    if spec.defaults is None:
        return {}

    ln = len(spec.defaults)
    
    return dict(zip(aa.args[-ln:], spec.defaults))




def checkCall(spec, argl, argd):

    defaults = getDefaultArgs(spec)
    deflen = len(spec.defaults) if spec.defaults is not None else 0
    args = len(spec.args)

    kwargs = len(set(spec.args) and set(argd.keys()))

    return len(argl) >= args - deflen - kwargs



class Curry(object):

    def __init__(self, func, *argl, **argd):

        f, args = getFunc(func)
        
        self.function = f
        
        self.argspec = inspect.getargspec(func)

        self.argl = args + argl
        self.argd = argd


    def __call__(self, *argl, **argd):

        newArgl = self.argl + argl
        newArgd = dict(self.argd, **argd)

        if checkCall(self.argspec, newArgl, newArgd):
            return self.function(*newArgl, **newArgd)
        else:
            return Curry(self.function, *newArgl, **newArgd)



