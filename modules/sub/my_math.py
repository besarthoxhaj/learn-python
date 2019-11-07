import modules.sub_dir.add_num as numStuff


def add(a, b):
    return a + b


def addToTwo(num):
    print 'addToTwo: adding 2 to', num
    return numStuff.two(num)
