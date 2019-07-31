import requests
from addbook import *
from requests import get
from bs4 import BeautifulSoup
names = ['Name']
authors = ['Author']
genres = ['Genre']
raw = ['Business', 'Computer', 'Literature & Fiction', 'Science & Math',
       'Mystery', 'History', 'Religion', 'Medical', 'Sports', 'Arts']
url = ['https://www.amazon.com/Best-Sellers-Books-Business-Money/zgbs/books/3', 'https://www.amazon.com/Best-Sellers-Books-Computers-Technology/zgbs/books/5/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Literature-Fiction/zgbs/books/17/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Science-Math/zgbs/books/75/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Mystery-Thriller-Suspense/zgbs/books/18/ref=zg_bs_nav_b_1_b',
       'https://www.amazon.com/Best-Sellers-Books-History/zgbs/books/9/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Religion-Spirituality/zgbs/books/22/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Medical/zgbs/books/173514/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Sports-Outdoors/zgbs/books/26/ref=zg_bs_nav_b_1_b', 'https://www.amazon.com/Best-Sellers-Books-Arts-Photography/zgbs/books/1/ref=zg_bs_nav_b_1_b']
k = 0
for l in range(0, 10):
    i = 0
    response = get(url[k])
    html_soup = BeautifulSoup(response.text, 'html.parser')
    book_containers = html_soup.find_all('div', class_='zg_itemWrapper')
    for book in book_containers:
        name = ((book.find('div', class_='p13n-sc-truncate p13n-sc-line-clamp-1').get_text())).strip()
        names.append(name)

        author = book.find('a', class_='a-size-small a-link-child')
        if author is not None:
            author = ((book.find('a', class_='a-size-small a-link-child').get_text())).strip()
        else:
            author = "Not available"
        authors.append(author)
        genres.append(raw[k])
        i += 1
        if(i > 10):
            break
    k += 1
length = len(names)
for i in range(1, length):
  Add(names[i],authors[i],genres[i])
