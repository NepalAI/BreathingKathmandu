from urllib.request import urlopen
from bs4 import BeautifulSoup

myLink = "https://en.wikipedia.org/wiki/Particulates"

page = urlopen(myLink)

pageSource = BeautifulSoup(page, "lxml")
# print(pageSource)

# extract all tables
all_tables = pageSource.find_all('table')

# get the right table by defining its class
right_table = pageSource.find('table', class_='wikitable')
x = format(right_table)
cleantext = BeautifulSoup(right_table, "lxml").text
print(cleantext)