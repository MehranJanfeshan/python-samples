# Accepts args as param in function, args lets you to pass as many param az you like to the function
# Args is not a keyword and can be replace with any arbitrary word
# Args returns back tuples
def my_func_args(*args):
    print(args)


# Accepts kwargs as param in function, kwargs lets you to pass as many param az you like to the function
# kwargs is not a keyword and can be replace with any arbitrary word
# kwargs returns back dictionary
def my_func_kwargs(**kwargs):
    print(kwargs)


# use args and kwargs together
def my_func_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


my_func_args(1, 2, 4, 5, 6, 7)
my_func_kwargs(name='mehran', lasname='james', code=123)
my_func_args_kwargs(1, 2, 3, 4, 5, name='mehran', lasname='james', code=123)
