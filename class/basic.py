# coding: utf-8

x = 4
y = x
print("x:{}".format(x))
print("y:{}".format(y))
print("x=y:{}-{}".format(id(x), id(y)))
x = "abc"
print("x:{}".format(x))
print("y:{}".format(y))
print("x=y:{}-{}".format(id(x), id(y)))
y = 19
print("x:{}".format(x))
print("y:{}".format(y))
print("x=y:{}-{}".format(id(x), id(y)))
