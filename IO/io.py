# Open a file
my_file = open('myfile.txt')

# Read the whole file! maybe not the good idea!
print(my_file.read())

#  if you try to read the file again, you get back nothing
#  because the file is open and the cursor is at the end of the file
print(my_file.read())

# Move the cursor to the beginning of the file
my_file.seek(0)
print(my_file.read())

# Read line by line
my_file.seek(0)
print(my_file.readlines())  # This command returns back a list!

# Close file after opening it!
my_file.close()

# Modern way of working with file! by doing this you do not need to close the file after you are done with it!
with open('myfile.txt') as my_new_file:
    content = my_new_file.read()
    print(content)


# r: read
# w: write
# a: append
# Open the file only for reading
with open('myfile.txt', mode='r') as r:
    readContent = r.read()
    print(readContent)

# Open the file only for writing
with open('myfile_for_writing.txt', mode='w') as f:
    f.write('This is writing to file')

# Open the file only for writing
with open('myfile_for_appending.txt', mode='a') as a:
    a.write('This is appending to file')

# Appending to the file
with open('myfile_for_appending.txt', mode='r') as ra:
    appendContent = ra.read()
    print(appendContent)


# Creating completely a new file
with open('my_new_file.txt', mode='w') as nw:
    nw.write('This is a new file!')



