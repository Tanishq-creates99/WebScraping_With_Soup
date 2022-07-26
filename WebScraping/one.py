from bs4 import BeautifulSoup
import requests

website = "http://automationpractice.com/index.php?id_category=3&controller=category"

response = requests.get(website)

print(response.status_code)

soup = BeautifulSoup(response.content,'html.parser') #new variable = Bs(contentextraction,"the format which we need from structure ")

contact_us = soup.find(id='contact-link').get_text().replace('\n','')#.getonly text .replace space with no space
#print(contact_us)
                         #OOORRRRR
#contact_us = soup.find('div',{'id':'contact-link'}).get_text()                         

contact_us2 = soup.find(id='contact-link').find('a')#find with class ID and specify the tag ie a tag here
#print(contact_us2)

#-------whenever u want to search something by class use _at the end and start with .forattributes 
result = soup.find(class_ ='ajax_block_product')
print(result)


findall = soup.find_all(class_ ="ajax_block_product")
print(len(findall))
