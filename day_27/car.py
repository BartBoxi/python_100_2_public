# def foo(a, b=4, c=6):
#     print(a,b,c)
#
# print(foo(4,8,9))


# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        #self.year = kwargs["year"]


my_car = Car(make="Nissan", model="GTR")
print(my_car.make)