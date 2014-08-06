List = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

Map = {
    'func1': lambda x: x**2,
    'func2': lambda x: x**3,
    'func3': lambda x: x**4,
}

Lower = lambda x,y: x if x<y else y

from sys import stdout
Show = lambda x: map(stdout.write, x)
ShowAll = lambda lines: [Show(line) for line in lines]

Nested = lambda x: (lambda y: x + y)