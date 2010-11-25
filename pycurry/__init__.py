#-*- coding:utf-8 -*-

import curry


def curryfunc(func):

    return curry.CurryFunction(func)



def test():

    @curryfunc
    def func(a, b, c):

        print a, b, c


    @curryfunc
    def func2():
        print 'hello'


    print func(10)
    func(10, 20, 30)
    func(10, 20, c=50)

    func2()


if __name__ == '__main__':
    test()

