#! python3

# Web Scraper which will scrape latest schemes from a farmer relate news website when run
 
import requests, bs4, json

url = 'https://krishijagran.com/agripedia/best-government-schemes-and-programmes-in-agriculture-for-farmers/'
data = {}
data['scheme'] = []

# Get the page and check for any HTTP error while doing so
res = requests.get(url)
res.raise_for_status()

# Retrieve the data of the site
soup = bs4.BeautifulSoup(res.text,'lxml')

# Fetch all the headings of the Schemes
for child in soup.find_all("h3"):
	if(child.contents[0].name == "strong"):
		title = child.string;

		details = child.find_next_sibling('p');
		info = details.text.strip()

		link = "https://farmer.gov.in"
		if(details.find('a', href=True)):
			link = details.find('a', href=True)['href']
			# in case the link is relative
			if(not link.startswith("http")):
				link = "https://krishijagran.com" + link;

		# putting everything in json foromat
		data['scheme'].append({
		    'title': child.string,
		    'details': info,
		    'link': link
		})

# putting stuff in json file
with open('results.json', 'w') as outfile:
    json.dump(data, outfile)