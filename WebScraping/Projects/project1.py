from bs4 import BeautifulSoup
import requests
import pandas as pd

website = "https://books.toscrape.com/"
responses = requests.get(website)

soup = BeautifulSoup(responses.content,'html.parser')
results = soup.find_all('li',{'class':'col-xs-6'})
#print(len(results))

product = results[0]
PProduct  = product.find('h3').find('a').get('title')
#print(PProduct)

product_price = product.find(class_='price_color').get_text()
#print((product_price))
product_availability = product.find(class_='instock availability').get_text().strip()
#print(product_availability)


book_name = [result.find('h3').find('a').get('title') for result in results] 
#print(book_name)

Price = [result.find(class_='price_color').get_text() for result in results]
#print(Price)

avail = [result.find(class_='instock availability').get_text().strip() for result in results]
#print(avail)

info = pd.DataFrame({'name':book_name,'Price':Price, 'Availability':avail})
#print(info)

#info.to_excel('BOOKS_Results.xlsx',index=False)