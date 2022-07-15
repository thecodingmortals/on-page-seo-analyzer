# import urllib.request
# # import urlllib2
# # try:
# #     from urllib.request import Request, urlopen  # Python 3
# # except ImportError:
# #     from urllib2 import Request, urlopen  # Python 2
# myfile = None
# link = "http://www.somesite.com/details.pl?urn=2344"
# with urllib.request.urlopen (link) as url:
        
#         myfile = url.read()
# print(myfile)


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

import ipdb;ipdb.set_trace()

driver = webdriver.Chrome(ChromeDriverManager().install())

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("<a href=https://www.flipkart.com/laptops/>https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
   name=a.find('div', attrs={'class':'_3wU53n'})
   price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
   rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
   products.append(name.text)
   prices.append(price.text)
   ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')