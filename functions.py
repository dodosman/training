# def star_wars_hello():
#    return "hello there\nGENERAL KENOBI"
#
# print(star_wars_hello())

# def hello_func(greeting, name='Dominik'):
#     return "{}, {}.".format(greeting, name)
#
#
# print(hello_func('Hello ', 'Cortney'))

# def student_info(*args, **kwargs):
#     print(args,kwargs)
#
# student_info('Matthew',21, 'Sociology',name = 'john', age = 22 )
#


def get_real_floor(n):
    if n >= 1:
        return n - 1
    elif n <= 0:
        return n
    elif n == 13:
        return "15"
    else:
        return n


def userHello(UserName):
    print("witam Cię,", UserName, "w moim programie")


UserNames = ['Castelgandolfo', 'Kutafiks', 'Michałek', 'Domino']
#
# for UserName in UserNames:
#     userHello(UserName)

# greeting = [userHello(UserName)
#             for UserName in UserNames]

