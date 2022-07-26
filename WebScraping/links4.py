from bs4  import BeautifulSoup
import requests

website = "http://automationpractice.com/index.php?id_category=3&controller=category"
response = requests.get(website)
#print(response.status_code)

soup = BeautifulSoup(response.content,'html.parser')

single_link = soup.find(id = 'contact-link').find('a')['href']
#print(single_link)

Multiple_link = soup.find_all(itemprop = 'name')
print(Multiple_link)

links = [] 
for a in Multiple_link:
    links.append(a.find('a')['href'])
    