def func():
    print('Func() IN ONE.PY')


print('Top level in one.py')

# if name = __main__ it means that file is called directly from the CLI
if __name__ == '__main__':
    print('One.Py is being run directly!')
else:
    print('One.PY has been imported!')
