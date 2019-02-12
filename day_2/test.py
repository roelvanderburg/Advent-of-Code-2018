for i in range (5):
    print("i is: ", i)
    for j in range(3):
        if j ==2:
            break
        print("Jee is: ",  j)


class Foo(object):
    def __init__(self, name):
        self.name = name

name = "Hello"
foo = Foo(name)
name[0] = "J"