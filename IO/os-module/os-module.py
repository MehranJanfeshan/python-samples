import os

# Get the current directory you are at!
print(os.getcwd())

# List the current directory
print(os.listdir())

# List the directory that you path
print(os.listdir('/Users'))

# remove the file at the given path
# os.unlink(path)


# delete the folder at the given path, folder must be empty
# os.rmdir(path)

# os.walk returns the list of all file, subFolders - it looks at all the subFolders and check all the files

for folder, subFolders, files in os.walk('/Users/mehran.janfeshan/code/python-sample'):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subFolders are:")
    for subFolder in subFolders:
        print(f"The subFolder: {subFolder}")

    print("\n")
    print('The files are:')
    for file in files:
        print(f"The file si: {file}")
