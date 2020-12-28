#! python3

# Web Scraper which will scrape latest schemes from the government website when run 
 
import requests, bs4, json

url = 'https://krishijagran.com/agripedia/best-government-schemes-and-programmes-in-agriculture-for-farmers/'

# Get the page and check for any HTTP error while doing so
res = requests.get(url)
res.raise_for_status()

# Retrieve the data of the site
soup = bs4.BeautifulSoup(res.text,'lxml')

# Fetch all the headings of the Schemes
for child in soup.find_all("h3"):
	if(child.contents[0].name == "strong"):
		print(child.string)