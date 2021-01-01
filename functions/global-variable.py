x = 50


# To change the global variable you have to use global keyword!
# You can access the global variable without using global keyword
# It is better to not use global keyword as it makes it very difficult to see where the change is happening
def func():
    global x
    print(f"This is global X inside the func function {x}")
    x = 100


func()
print(f'This is global X outside of the func function {x}')
