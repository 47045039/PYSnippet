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

if True:
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

if True:
    import args
    print args.minmax(lambda x, y: x < y, 1,4,7,2,5,8,3,6,9)    # 1
    print args.minmax(lambda x, y: x > y, 1,4,7,2,5,8,3,6,9)    # 9
    
    def lessthan(x, y): return x < y
    def morethan(x, y): return x > y
    print args.minmax(lessthan, 1,4,7,2,5,8,3,6,9)  # 1
    print args.minmax(morethan, 1,4,7,2,5,8,3,6,9)  # 9

if True:
    import args
    print args.intersect([1,2,3,4,5,6], [3,4,5,6,7,8], [5,6,7,8,9]) # [3, 4, 5, 5, 6, 6]
    print args.union([1,2],[3,4],[5,6])                             # [1, 2, 3, 4, 5, 6]
    
    print args.intersect('abcde', 'cdefg')  # ['c', 'd', 'e']
    print args.union('abcde', 'cdefg')      # ['a', 'b', 'c', 'd', 'e', 'f', 'g']


    