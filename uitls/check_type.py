# coding: utf-8
import numpy as np
import pandas as pd

# http://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
o = None
# To check if an object o is a string type of a subclass of a string type:

# To check if the type of o is exactly str:

type(o) is str
# To check if o is an instance of str or any subclass of str:

isinstance(o, str)

# Python: Check if a string represents an int, Without using Try/Except?
print('16'.isdigit())


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


print(check_int("16.5"))
print("99999")
print("5.6".isnumeric())

'''
字符串比较 is 和==不同
is is identity testing, == is equality testing. what happens in your code would be emulated in the interpreter like this:
'''
a = 'pub'
b = ''.join(['p', 'u', 'b'])
print(a == b)
print(a is b)

a = [['a', '1.2', '4.2'], ['b', '7b', '0.03'], ['x', '5', '0']]
df = pd.DataFrame(a, columns=['one', 'two', 'three'])
print(df)
print(df.dtypes)

df[['two', 'three']] = df[['two', 'three']].astype(float, raise_on_error=False, )

print(df)
print(df.dtypes)


# 列转换为numeric，coerce是当值不为numeric时会转换为NaN

df["one"] = pd.to_numeric(df["one"], errors="coerce")
df["two"] = pd.to_numeric(df["two"], errors="coerce")

# df["one"]=df.apply(pd.to_numeric())

print(df)
