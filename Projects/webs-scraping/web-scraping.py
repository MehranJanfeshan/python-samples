import requests
import bs4

# Calls the endpoint and gets the result
result = requests.get("https://www.example.com")

# Beautifuler the response
soup = bs4.BeautifulSoup(result.text, "lxml")

# extracts the tag from the response and returns the list
print(soup.select('title'))

# Returns the text of that object!
print(soup.select('h1')[0].getText())
