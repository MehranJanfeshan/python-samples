import requests
import bs4

# Calls the endpoint and gets the result
result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

# Beautify the response
soup = bs4.BeautifulSoup(result.text, "lxml")

# Extract the image tag base on the class name and get the first item found
computer = soup.select('.thumbimage')[0]

# Download the image src and add https at the beginning to create a URL
image_link = "https:" + computer['src']

# Get the image
image_link_content = requests.get(image_link)

# Create a file
f = open('my_computer.jpg', 'wb')

# Write the downloaded image to the file
f.write(image_link_content.content)

# Close the file at the end
f.close()
