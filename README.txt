=> This is a ref file with project to understand webscraping with the help of Beautiful Soup

==>>Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files.
It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

we import BeautifulSoup from Bs4
along with that requests 
and Pandas (in case of transferring multiple data pages to excel sheets .

1. import libraries 
2. request a get command for website // if required check status code for confirmation
3. use soup with request.content (content extraction) and parse it with 'html.parser'
4. create a variable 
5. we use find or find_all commands to get data 
6. find(id="").find('tag') // if required to get specific text use .get_text() and also strip()
   class name should have an _ in find
7. we also used selector , here we can call class by using . at start unlike _ at the end of class
   eg. select = select_one('.shop_name').get_text().strip().replace('call now :','')
8. we can also add multiple links in here 
  eg . links = [] 
        for a in Multiple_link:
         links.append(a.find('a')['href'])
         print(link)
