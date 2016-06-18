import sys

def sayHello(name):
    """"Print 'Hello ${name}' to stdout"""
    print 'Hello', name

# print(dir(sayHello))
# # [
# #   '__call__',
# #   '__class__',
# #   '__closure__',
# #   '__code__',
# #   '__defaults__',
# #   '__delattr__',
# #   '__dict__',
# #   '__doc__',
# #   '__format__',
# #   '__get__',
# #   '__getattribute__',
# #   '__globals__',
# #   '__hash__',
# #   '__init__',
# #   '__module__',
# #   '__name__',
# #   '__new__',
# #   '__reduce__',
# #   '__reduce_ex__',
# #   '__repr__',
# #   '__setattr__',
# #   '__sizeof__',
# #   '__str__',
# #   '__subclasshook__',
# #   'func_closure',
# #   'func_code',
# #   'func_defaults',
# #   'func_dict',
# #   'func_doc',
# #   'func_globals',
# #   'func_name'
# # ]
# print(sayHello.__doc__)
# # Print 'Hello ${name}' to stdout
# print(sayHello)
# # <function sayHello at 0x10c5f6c80>

sayHello(sys.argv[1])
