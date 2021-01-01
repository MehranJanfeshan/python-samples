string_number = '100'
# Check if the string is digit!
print(string_number.isdigit())

# Converting string to number
print(int('100'))

accepted_values = [1, 3, 5, 7]


def user_choice():
    choice = 'wrong'

    while not choice.isdigit():
        choice = input('Please enter a number')

    if choice in accepted_values:
        print('You keyed in a correct input')

    if choice not in accepted_values:
        print('You keyed in a correct input')


user_choice()
