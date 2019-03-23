import urllib.request
import bs4
import json

def main():
	colors_page = 'https://encycolorpedia.com/named'

	headers = {'User-Agent': 'Mozilla/5.0'}

	req = urllib.request.Request(colors_page, headers={'User-Agent': 'Mozilla/5.0'})

	page = urllib.request.urlopen(req).read()

	soup = bs4.BeautifulSoup(page, 'html.parser')
	ol_items = soup.find('ol')
	li_items = ol_items.find_all('li')

	i = 0
	while i < len(li_items):
		link_item = li_items[i].find('a')
		value = link_item['href']
		print(value)
		print(link_item.text.split('#')[0].split('(')[0])
		i += 1

if __name__ == '__main__':
    main()
