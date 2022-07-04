from bs4 import BeautifulSoup as sp
import requests

url = 'https://www.geeksforgeeks.org/'
# url_instance = ScrapedWebpag(url)


class ScrapedWebpag:
    
    def __init__(self,url):
        self.url = url
        self.set_title()
        
        
    def get_internal_links(self):
        reqs = requests.get(self.url)
        soup = sp(reqs.text, 'html.parser')
        
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
        # print(urls)    
  
    def set_title(self):

      reqs = requests.get(self.url)
      soup = sp(reqs.text, 'html.parser')
      con = soup.find('a', class_="head")
      a = con.get('title')
      self.title = a.strip('Permalink to GeeksforGeeks Job-')
      
    
    def __getwordcount__(self):

        wordCount = 0;  
   
        for i in range(0, len(self.title)-1):  
            
            if(self.title[i] == ' ' and self.title[i+1].isalpha() and (i > 0)):  
                wordCount = wordCount + 1;    
        wordCount = wordCount + 1;  
           
        print("Total number of words in the given string: " + str(wordCount));  



def main():
    obj = ScrapedWebpag(url)
#     # obj.set_title(url)
    obj.__getwordcount__()

if __name__ == "__main__":
    main()