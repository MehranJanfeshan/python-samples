import datetime
# This only contains date!
# you can pass, hour, minute, second, micro second
my_time = datetime.time(2, 20)

print(my_time.minute)

print(my_time.hour)

print(my_time.second)

# get the current date - european date
print(datetime.date.today())

print(datetime.date.today().year)

print(datetime.date.today().month)

print(datetime.date.today().day)

print(datetime.date.today().ctime())


