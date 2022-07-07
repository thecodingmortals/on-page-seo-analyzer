from bs4 import BeautifulSoup as soup
import requests


class ScrappedImage:

    def __init__(self,alt_text, url_source):
        self.url_source = url_source
        self.alt_text = alt_text


    def has_alt_text(self):
               
        '''Return a bool value where True is returned,
        if there is an alt text present for the given image.
        '''       
        
        return bool(self.alt_text)        


    def to_representation(self):

        dict = {
            "url_source": self.url_source ,
            "alt_text": self.alt_text
        }

        return dict
        

img_source = ""
alt_text = ""
def get_alt_text(url):

    reqs = requests.get(url)
    soup1 = soup(reqs.text, 'html.parser')
    
    con = soup1.find('div', class_="banner-img").find('img')
    conn = '<img alt="GEEK-O-LYMPICS 2022 - May The Geeks Force Be With You!" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220630162102/GEEK-O-LYMPICS-2022-May-The-Geeks-Force-Be-With-You.png"/>'
        
    soup1 = soup(conn,
                features="html.parser"
            )

    img_source = soup1.find("img")['src']
    alt_text = soup1.find("img")["alt"]
    lis = [img_source,alt_text]
    return (lis)
   
   
def main():

    url = 'https://www.geeksforgeeks.org/'
    ab = get_alt_text(url)
    alt_text = ab[0]
    img_source = ab[1]

    obj = ScrappedImage(alt_text,img_source)
    print(obj.to_representation())

   
if __name__ == "__main__":
    main()    
        



