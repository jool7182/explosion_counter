from bs4 import BeautifulSoup
import requests


#gets html tags, finds <a> tags
html_text = requests.get('https://en.wikipedia.org/wiki/List_of_explosions#Prior_to_2000').text
soup = BeautifulSoup(html_text, 'lxml')
sites = (soup.find_all('a'))

#puts tags in a list
result = []
for country in sites:
    a = str(country.get('href'))
    result.append(a)

#Converts tags to strings
webs = ''
for item in result:
    webs = webs.lower() + item + '\n'

#remove unnecessary string elements
sub_str = '#cite_note-459'
new_string = webs.split(sub_str)
product = new_string[0]+sub_str

#Gets user input and counts
country = input('Type the name of a country to see how many major explosions it has experienced in its history: ')
country = country.lower()
final = product.count(country)
if final > 1 or final < 1:
    print(f'{country.title()} has experienced {final} major explosions')
else:
    print(f'{country.title()} has experienced {final} major explosion')


