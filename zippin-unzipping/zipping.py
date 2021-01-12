import zipfile

# Creating two files!
f = open('fileOne.txt', 'w')
f.write('File One')
f.close()

f = open('fileTwo.txt', 'w')
f.write('File Two')
f.close()

# Create an emtpy zip file
comp_file = zipfile.ZipFile('com_file.zip', 'w')

comp_file.write('fileOne.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('fileTwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
