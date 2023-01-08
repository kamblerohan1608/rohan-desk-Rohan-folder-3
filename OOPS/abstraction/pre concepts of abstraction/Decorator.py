
# Decorator.

# a very powerful tool which can modify a function from outide of function without changing or accessing it.

# def decor_div(function):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return function(a,b)
#     return inner


# @decor_div
# def div(a,b):
#     return a/b

# print(div(10,2))
# print(div(2,10))

# Example 2


def decor_per(function):
    def inner(obtain,total):
        if obtain>total:
            obtain,total = total,obtain
        return function(obtain,total)
    return inner


@decor_per
def per(obtain,total):
    return (obtain*100)/total

print(per(10,2))
print(per(2,10))

