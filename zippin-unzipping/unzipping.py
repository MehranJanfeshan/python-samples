import zipfile

zip_obj = zipfile.ZipFile('com_file.zip')

# Extract everything to the defined folder
# It creates folder if does not exist
zip_obj.extractall('extract_content')
