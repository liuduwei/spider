import requests
import re


url = 'https://static1.scrape.cuiqingcai.com/' 
r = requests.get(url)
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
result = re.findall(pattern, r.text)
print(result)
