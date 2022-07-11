import json
import requests

class WebsiteStatusCode:
    def __init__(self, lis):
        '''It will contain the list of all urls.'''
        self.urls = lis           

    def get_URL_status_codes(self): 
        '''It will make a dictionary of urls and their status code
           if status code gets a value 301, it will be redirected
           to the new usrl and return the status of 200.
        '''
        dic ={}
        for url in self.urls:
           r = requests.get(url,allow_redirects=False)
           r.status_code
           dic[url] = {}
           dic[url][url] = r.status_code
           if r.status_code in [301,302]:
             r = requests.head(url, allow_redirects=True)
             dic[url][r.url] = r.status_code
        return (json.dumps(dic, indent=4))



