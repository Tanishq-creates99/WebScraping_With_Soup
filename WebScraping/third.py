from bs4 import BeautifulSoup
import requests

website = "http://automationpractice.com/index.php?id_category=3&controller=category"
response = requests.get(website)

soup = BeautifulSoup(response.content,'html.parser')

attribute = soup.find(itemprop='name').find('a').get('title')
print(attribute)
#both provide same value except get needs to be specific with attribute
#where as get_text directly gives tect wuth unnecessary \n\t which can  be removed by .strip
attribute1 = soup.find(itemprop='name').find('a').get_text().strip()
#print(attribute1)

sibling = soup.select_one('.ajax_block-product').find_next_sibling().select_one('product-name').get_text()
print(sibling)


