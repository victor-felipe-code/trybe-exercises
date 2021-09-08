import requests
from parsel import Selector

url = "http://books.toscrape.com/"

response = requests.get(url)
selector = Selector(text=response.text)
# print("STATUS CODE -->", response.status_code)
# [print(x) for x in selector.css("img.thumbnail").getall()]

thumbnail_url_selector = "div.image_container a::attr(href)"

for url_x in selector.css(thumbnail_url_selector).getall():
    thumbnail_request = requests.get(url + url_x)
    thumbnail_selector = Selector(text=thumbnail_request.text)
    book_title = thumbnail_selector.css("div.product_main h1")
    print(book_title.get())
