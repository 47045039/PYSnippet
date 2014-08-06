def f1(a=1, b=2, c=3):
    print a, b, c

def f2(*args):
    print args

def f3(**args):
    print args

def f4(a=-1, b=-2, *args, **args2):
    print a, b, args, args2

def minmax(func, *args):
    var = args[0]
    for arg in args[1:]:
        if func(arg, var):
            var = arg
    return var

def intersect(*args):
    res = []
    for x in args[0]:
        for arg in args[1:]:
            if x not in arg:
                break;
            else:
                res.append(x)
    return res

def union(*args):
    res = []
    for arg in args:
        for x in arg:
            if x not in res:
                res.append(x)
    return res    

