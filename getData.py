
from bs4 import BeautifulSoup
import requests
import json
 
url = "https://apps.cs.utexas.edu/calendar/"
 
# Getting the webpage, creating a Response object.
response = requests.get(url)
 
# Extracting the source code of the page.
data = response.text
 
# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a', class_="colorbox-load")
 
# Extracting URLs from the attribute href in the <a> tags.

event_dict = {
    
}

def parseFiles():
    tags = soup.find_all('a', class_="colorbox-load")
    parturl = "https://apps.cs.utexas.edu"
    for tag in tags:
        tagtext = tag.get('href')
        fullurl = parturl + tagtext
        response2 = requests.get(fullurl)
        data2 = response2.text
        soup2 = BeautifulSoup(data2, 'lxml')
        
        title = soup2.find('h1',attrs={'id':'page-title'}).getText()
        date = soup2.find('span',attrs={'class':'date-display-single'}).getText()
      
        
        event = {
            title:{
                'date': date,
                'url': fullurl
            }
        }
        event_dict[title] = event[title]
        

parseFiles()
jsondict = json.dumps(event_dict)
print(jsondict)