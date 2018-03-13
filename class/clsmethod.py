# coding: utf-8

class A(object):
    def foo(self, x):
        print("executing foo({},{})".format(self, x))
        print("self:{}".format(self))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo({},{})".format(cls, x))
        print("self:{}".format(cls))

    @staticmethod
    def static_foo(x):
        print("executing static_foo({})".format(x))


a = A()

a.foo(3)
a.class_foo(3)
a.static_foo(3)
A.class_foo(3)
A.static_foo(3)

A.foo(a, 3)
