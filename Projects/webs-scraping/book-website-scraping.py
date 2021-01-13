import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# 1 will replace {}
res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')

products = soup.select('.product_pod')

example = products[0]

# check if the tag has specific string
print('star-rating Three' in str(example))

# check if there is a tag with a specific class name
# if class name has white space you must cover it with .
print(example.select(".star-rating.Three"))
print(example.select(".star-rating.Two"))

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)

print(len(soup.select('.product_pod')))
