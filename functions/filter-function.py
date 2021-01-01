# Filter function
def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


my_nums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, my_nums)))


