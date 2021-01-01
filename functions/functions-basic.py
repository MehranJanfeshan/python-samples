def name_of_function(name):
    # hi man
    print(f"hello {name}")


def default_value(name='Mehran'):
    print(f"hello {name}")


def check_even(number):
    return number % 2 == 0


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


# Use pass within a function
def return_even_list(num_list):
    even_number = []
    for number in num_list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number


# Returns back Tuples from a function
def employee_check():
    work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return employee_of_month, current_max


name_of_function("Mehran")
default_value()
print(check_even(10))
print(check_even(11))
print(check_even_list([1, 3, 5, 7]))
print(check_even_list([1, 3, 5, 8]))
print(return_even_list([1, 3, 5, 8, 10, 11, 15]))
print(employee_check())
