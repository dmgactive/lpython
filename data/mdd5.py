# coding: utf-8


import hashlib

src = "what"
m2 = hashlib.md5()
m2.update(bytes(src, 'UTF-8'))
print(m2.hexdigest())

print(hashlib.md5(src.encode()).hexdigest())


def get_hashkey(*values):
    str_source = ""
    for value in values:
        str_source = str_source + str(value)

    return hashlib.md5(str_source.encode()).hexdigest()


if __name__ == '__main__':
    print(get_hashkey("what", 5, "ou"))
