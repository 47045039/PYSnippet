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

if True:
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


    