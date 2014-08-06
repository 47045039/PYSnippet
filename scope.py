var = 100

def local():
    var = 0

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import scope
    scope.var += 1    

def glob3():
    var = 0
    import sys
    glob = sys.modules['scope']
    glob.var += 1

def test():
    print var
    local()
    glob1()
    glob2()
    glob3()
    print var

def f1():
    x = 1
    def f2():
        print x
    return f2

def maker(N):
    def action(x):
        return x ** N
    return action;

def maker2(N):
    return lambda X=2: X ** N

def maker3():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts