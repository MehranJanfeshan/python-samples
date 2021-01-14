from PIL import Image

my_image = Image.open('sample.jpg')

print(my_image.size)

# if you use the same file name it will replace it, so be careful!
result = my_image.crop((12, 12, 40, 80)).save('modifiedImage3.jpg', 'JPEG')
my_image.resize((3000, 500)).save('modifiedImage1.jpg', 'JPEG')
my_image.rotate(90).save('modifiedImage2.jpg', 'JPEG')
