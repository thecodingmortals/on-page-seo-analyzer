from attr import attr
from bs4 import BeautifulSoup 
import requests


class ScrappedImage:
    def __init__(self, url, img_source=None, alt_text=None):
       self.url = url
       self.img_source = img_source
       self.alt_text = alt_text


    def get_image_attributes(self):
       reqs = requests.get(self.url)
       soup = BeautifulSoup(reqs.text, 'html.parser')
       
       image_tag = soup.find('div', class_="banner-img").find('img')          
       img_source =  image_tag['src']
       alt_text =   image_tag['alt']
       lis = [img_source,alt_text]
       return (lis)    

    def get_img_source(self):
       reqs = requests.get(self.url)
       soup = BeautifulSoup(reqs.text, 'html.parser')
       
       image_tag = soup.find('div', class_="banner-img").find('img')          
       img_source =  image_tag['src']
       return img_source

    def get_alt_text(self):
       reqs = requests.get(self.url)
       soup = BeautifulSoup(reqs.text, 'html.parser')
       
       image_tag = soup.find('div', class_="banner-img").find('img')          
       alt_text =   image_tag['alt']
       return alt_text    

    def has_alt_text(self):
        '''Return a bool value where True is returned,
           if there is an alt text present for the given image.
        '''       
        alt_text = self.get_alt_text()
        return bool(alt_text[1])        

    def to_representation(self):
        '''It will return the dictionary containing image source and alt text'''
        dict = {
            "img_source": self.get_img_source(),
            "alt_text": self.get_alt_text(),
        }
        return dict    

