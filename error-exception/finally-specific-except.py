def add(num1, num2):
    try:
        result = num1 + num2
    # Specific error
    except TypeError:
        print('Type error occurred!')
    except OSError:
        print('An OS error occurred!')
    except:
        print('Other exception occurred!')
    else:
        print('Add went well!')
    finally:
        print('I always run!')


add('2', 3)
