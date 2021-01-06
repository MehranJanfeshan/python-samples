from datetime import datetime
from datetime import date

my_time = datetime(2021, 10, 3, 14, 20, 1)

print(my_time)

# replace
my_time = my_time.replace(year=2022)
print(my_time)

# subtract  date
date1 = date(2021, 11, 3)
date2 = date(2021, 11, 4)

result = date2 - date1
print(result)

# subtract  date and time
date3 = datetime(2021, 10, 3, 14, 20, 1)
date4 = datetime(2022, 10, 3, 14, 20, 1)

result = date4 - date3

# convert everything to seconds
print(result.total_seconds())

# return the second portion
print(result.seconds)

