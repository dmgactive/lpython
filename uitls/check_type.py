# coding: utf-8


# http://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
o=None
# To check if an object o is a string type of a subclass of a string type:

# To check if the type of o is exactly str:

type(o) is str
# To check if o is an instance of str or any subclass of str:

isinstance(o, str)


# Python: Check if a string represents an int, Without using Try/Except?
'16'.isdigit()

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

'''
字符串比较 is 和==不同
is is identity testing, == is equality testing. what happens in your code would be emulated in the interpreter like this:
'''
a = 'pub'
b = ''.join(['p', 'u', 'b'])
print(a == b)
print(a is b)
