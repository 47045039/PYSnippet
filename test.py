if True:
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


    