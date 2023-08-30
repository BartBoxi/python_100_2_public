# def foo(a, b=4, c=6):
#     print(a,b,c)
#
# print(foo(4,8,9))


def add(*args):
    for n in args:
        print(n)

add(2,1,1)