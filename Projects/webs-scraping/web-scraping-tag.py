import requests
import bs4

# Calls the endpoint and gets the result
result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

# Beautify the response
soup = bs4.BeautifulSoup(result.text, "lxml")

# Extract the tag from the response and returns the list
for item in soup.select('.toctext'):
    print(item.text)

# Grab nav tag based on it's ID
print(soup.find("nav", {"id": "p-personal"}))
