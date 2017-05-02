# coding: utf-8


class Person():
    def __init__(self):
        self.__x = None

    def setx(self, value):
        self.__x = value

    def getx(self):
        return self.__x

    def delx(self):
        del self.__x

    x = property(getx, setx, delx)


class PersonOne():
    def __init__(self):
        self.__x = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x

    @staticmethod
    def hello():
        print("hello world")


def log(text):
    def deco(func):
        def wra(*args, **kw):
            print(text)
            func(*args, **kw)

        return wra

    return deco


@log("23")
def now():
    print("2017-04-06")


p = Person()
p.x = 123

print(p.x)
print(p.getx())

pone = PersonOne()
pone.x = 66
print(pone.x)

PersonOne.hello()

now()
