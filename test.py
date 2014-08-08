if False:
    if False:
        def test1(x, y):
            return x + y
    else:
        def test1(x, y):
            return x - y

    def test2(x, y):
        return x * y

    print test1(3, 2)   # 5

    print test2(3, 2)   # 6

    X = 3;

    def test3(y):
        global X
        X = 2;
        return X * y

    def test4(y):
        return X * y

    print test3(2)  # 4
    print test4(2)  # 4
    print X         # 2

if False:
    import scope
    scope.test() # 100 103
    scope.f1()() # 1

    f2 = scope.maker(2)
    print f2(3)     # 3 ** 2 = 9
    print f2(4)     # 4 ** 2 = 16

    f3 = scope.maker(3)
    print f3(3)     # 3 ** 3 = 27
    print f3(4)     # 4 ** 3 = 64

    f2 = scope.maker2(2)
    print f2()      # 2 ** 2 = 4
    print f2(3)     # 3 ** 2 = 9
    print f2(4)     # 4 ** 2 = 16

    f3 = scope.maker2(3)
    print f3()      # 2 ** 3 = 8
    print f3(3)     # 3 ** 3 = 27
    print f3(4)     # 4 ** 3 = 64

    acts = scope.maker3()
    for act in acts:
        print act(2)    # 0 1 4 9 16

if False:
    import args
    args.f1()               # 1 2 3
    args.f1(3, 2, 1)        # 3 2 1
    args.f1(c=1, b=2, a=3)  # 3 2 1
    args.f1(1, c=4, b=5)    # 1 5 4
##    args.f1(1, a=5, b=6)    # crash

    args.f2()               # ()
    args.f2(1)              # (1,)
    args.f2(1, 2, 3)        # (1, 2, 3)

    args.f3()               # {}
    args.f3(a=1, b=2)       # {'a': 1, 'b': 2}

    args.f4()                           # -1 -2 () {}
    args.f4(9, 8)                       # 9 8 () {}
    args.f4(9, 8, 1, 2, 3)              # 9 8 (1, 2, 3) {}
    args.f4(x=5, y=6)                   # -1 -2 () {'y': 6, 'x': 5}
    args.f4(9, 8, 1, 2, 3, x=5, y=6)    # 9 8 (1, 2, 3) {'y': 6, 'x': 5}

if False:
    import args
    print args.minmax(lambda x, y: x < y, 1,4,7,2,5,8,3,6,9)    # 1
    print args.minmax(lambda x, y: x > y, 1,4,7,2,5,8,3,6,9)    # 9

    def lessthan(x, y): return x < y
    def morethan(x, y): return x > y
    print args.minmax(lessthan, 1,4,7,2,5,8,3,6,9)  # 1
    print args.minmax(morethan, 1,4,7,2,5,8,3,6,9)  # 9

if False:
    import args
    print args.intersect([1,2,3,4,5,6], [3,4,5,6,7,8], [5,6,7,8,9]) # [3, 4, 5, 5, 6, 6]
    print args.union([1,2],[3,4],[5,6])                             # [1, 2, 3, 4, 5, 6]

    print args.intersect('abcde', 'cdefg')  # ['c', 'd', 'e']
    print args.union('abcde', 'cdefg')      # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

if False:
    x = 'abc'
    def func():
        print x # x为全局变量
    func()  # abc（全局变量）

    x = 'abcd'
    def func():
        x = 'bcde'  # x为局部变量
    func()
    print x     # abcd（全局变量）

    x = '12345'
    def func():
        x = 'abcd'
        print x # x为局部变量
    func()      # abcd
    print x     # 12345（全局变量）

    x = '34567'
    def func():
        global x    # x为全局变量
        x = 'abc'
    func()
    print x     # abc（全局变量）

    x = '345'
    def func():
        x = 'efg'
        def nested():
            print x     # efg（局部变量）
        nested()
    func()
    print x     # 345（全局变量）

    def func(a, b, c=3, d=4):
        print a,b,c,d
    func(1, *(5,6))     # 1 5 6 4


if False:
    def func(x):
        import function
        for f in function.List:
            print f(x)
    func(2)     # 4 8 16

    def func(name, x):
        from function import Map
        if Map.has_key(name):
            print Map[name](x)
        else:
            print 'It\'s not a valid function name:', name, ', valid function names:', Map.keys()
            print 'It\'s not a valid function name:' + name + ', valid function names:' + str(Map.keys())
    func('func1', 3)  # 3 ** 2 = 9
    func('func2', 3)  # 3 ** 3 = 27
    func('func3', 3)  # 3 ** 4 = 81
    func('func4', 3)  # It's not a valid function name: func4 , valid function names: ['func3', 'func2', 'func1']
                      # It's not a valid function name:func4, valid function names:['func3', 'func2', 'func1']

    def func():
        from function import Map
        print Map.keys()        # ['func3', 'func2', 'func1']
        print Map.values()      # [<function <lambda> at 0x21feed8>, <function <lambda> at 0x21fee60>, <function <lambda> at 0x21fede8>]
        print Map.iteritems()   # <dictionary-itemiterator object at 0x226ef18>
        print Map.viewkeys()    # dict_keys(['func3', 'func2', 'func1'])
        print Map.viewvalues()  # dict_values([<function <lambda> at 0x21feed8>, <function <lambda> at 0x21fee60>, <function <lambda> at 0x21fede8>])
        print Map.viewitems()   # dict_items([('func3', <function <lambda> at 0x21feed8>), ('func2', <function <lambda> at 0x21fee60>), ('func1', <function <lambda> at 0x21fede8>)])
    func()

    def func():
        from function import Lower
        print Lower('123', '456')
    func()      # 123

    def func():
        from function import Show, ShowAll
        Show('1234\n')      # 1234
        ShowAll(('1,2,3,4\n', '4,5,6,7\n', '7,8,9\n'))  # 1,2,3,4\n 4,5,6,7\n 7,8,9\n
    func()

    def func():
        from function import Nested
        print Nested(2)(3)      # 5

        f = Nested(5)
        print f(2)      # 7
        print f(4)      # 9
    func();

if False:
    from function import ApplayFunc
    print apply(ApplayFunc)         # 6
    print apply(ApplayFunc, (3,5,6))    # 14
    print ApplayFunc(*(3,5,6));         # 14

    from function import MapFunc, MapFunc2
    print MapFunc(2, [5, 6, 7])     # [7, 8, 9]
    print MapFunc(5, [5, 6, 7])     # [10, 11, 12]
    print MapFunc2([1, 2, 3], [2, 3, 4])     # [1, 8, 81]

    from function import FilterFunc
    print FilterFunc(3, *(1,6))     # range(1, 6) && > 3 = [4, 5]
    print FilterFunc(3, -1, 10, 2)  # range(-1, 10, 2) && > 3 = [5, 7, 9]

    from function import ReduceFunc
    from operator import add,mul
    print ReduceFunc(lambda x,y: x+y, [1,2,3,4])    # 1+2+3+4 = 10
    print ReduceFunc(lambda x,y: x*y, [1,2,3,4])    # 1*2*3*4 = 24
    print ReduceFunc(add, [1,2,3,4])    # 1+2+3+4 = 10
    print ReduceFunc(mul, [1,2,3,4])    # 1*2*3*4 = 24

if True:
    print [x for x in range(5)]     # [0, 1, 2, 3, 4]
    print [x * 2 for x in range(5) if x % 2 == 0]     # [0, 4, 8]
    print filter(lambda x: x%2 == 0, range(5))      # [0, 2, 4]
    print map(lambda x: x*2, filter(lambda x: x%2 == 0, range(5)))  # [0, 4, 8]
    print [(x,y) for x in 'abc' for y in 'de']  # [('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e')]
    print [(x,y) for x in range(3) if x%2 == 0 for y in range(4) if y%2 == 1]   # [(0, 1), (0, 3), (2, 1), (2, 3)], x=0/2, y=1/3

    M = [[1,4,7], [2,5,8], [3,6,9]]
    print [row[1] for row in M]     # [4, 5, 6]

    ARR = [('john',35,'mgr'), ('bob',20,'dev')]
    print [age for (name,age,job) in ARR]           # [35, 20]
    print map((lambda (name,age,job): age), ARR)    # [35, 20]
