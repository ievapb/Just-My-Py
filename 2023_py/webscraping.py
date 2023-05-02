from bs4 import BeautifulSoup
import requests


info = requests.get("https://foodbase.azurewebsites.net/Category/Product?product=Apricot%2C%20dried")
soup = BeautifulSoup(info.text, features="html.parser")
#name_it = soup.find("h2").text
#print(name_it.prettify())
table = soup.find("table",{"class":"table"})
table_info = [t.text.strip() for t in table.find_all("td")]

lith_elements = []
eng_elements = []
element_values = []
element_units = []
i = 0
for things in table_info:
    if i == 0 or i%4 == 0: lith_elements.append(things)       
    if i == 1 or i%4 == 1: eng_elements.append(things)
    if i == 2 or i%4 == 2: element_values.append(things)
    if i == 3 or i%4 == 3: element_units.append(things)
    i += 1

print (eng_elements)
print(len(lith_elements), len(eng_elements), len(element_values), len(element_units))