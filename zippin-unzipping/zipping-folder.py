import shutil

# Zip the entire folder
dir_to_zip = '/Users/mehran.janfeshan/code/python-sample/zippin-unzipping/extract_content'

output_filename = 'example'

shutil.make_archive(output_filename, 'zip', dir_to_zip)

# Unzip the entire folder
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
