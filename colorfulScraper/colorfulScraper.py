import urllib.request
import bs4
import re
import json
import operator

def main():
	colors_page = 'https://encycolorpedia.com/named'

	req = urllib.request.Request(colors_page, headers={'User-Agent': 'Mozilla/5.0'})

	page = urllib.request.urlopen(req).read()

	print('Target acquired')

	soup = bs4.BeautifulSoup(page, 'html.parser')
	ol_items = soup.find('ol')
	li_items = ol_items.find_all('li')
	data = {}

	for list_item in li_items:
		link_item = list_item.find('a')
		value = link_item['href'].upper()
		value = re.sub('[/]', '#', value)
		color_name = link_item.text.split('#')[0].split('(')[0]
		color_name_words = re.split('[^a-zA-Z0-9]', color_name)
		culled_words = []
		is_first_word = True
		for word in color_name_words:
			if word.isalnum():
				if (is_first_word):
					is_first_word = False
					culled_words.append(word.lower())
				else:
					culled_words.append(word.capitalize())
		camel_case_name = ''.join(culled_words)

		data[camel_case_name] = value

	print('All the colors pulled. Just one moment please...')
	sorted_data = sorted(data.items(), key=operator.itemgetter(1))
	with open('colors.json', 'w') as jsonfile:
		json.dump(sorted_data, jsonfile)

	print('Done')

if __name__ == '__main__':
    main()
