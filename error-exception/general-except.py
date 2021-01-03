def add(num1, num2):
    try:
        result = num1 + num2
    # Generic error
    except:
        print('Something went wrong!')
    else:
        print('Add went well!')
        print(result)


add(1, 2)
