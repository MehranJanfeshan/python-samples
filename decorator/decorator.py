def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')

    return wrap_func


def fun_needs_decorator():
    print('I want to be decorated!')


# This is what actually happens behind the sense of decorator
decorator_func = new_decorator(fun_needs_decorator)

decorator_func()


# You do not need what we have done above, you can use decorator to run decorator and it saves you a lot of time!
@new_decorator
def fun_needs_decorator2():
    print('I want to be decorated2!')


fun_needs_decorator2()
