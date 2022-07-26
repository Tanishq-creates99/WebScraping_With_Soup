from bs4 import BeautifulSoup
import requests

website = "http://automationpractice.com/index.php?id_category=3&controller=category"
response = requests.get(website)
print(response.status_code)

soup = BeautifulSoup(response.content,'html.parser')

#select one is same as find 
#but since its css selector we need to put  A  . before start for class
select = soup.select_one('.shop-phone')
#print(select)

select1 = soup.select_one('.shop-phone').get_text().strip()
#instead of using .remove("\n",')we use strip which removes empty spaces

#print(select1)
select2 = soup.select_one('.shop-phone').get_text().strip().replace('Call us now: ','')
print(select2)