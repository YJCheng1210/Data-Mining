import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def stock(code):
    res = requests.get(
        f'https://www.google.com/search?q={code}+stock&oq={code}+stock&aqs=chrome.0.69i59j0i131i433i512j0i512l8.2291j1j9&sourceid=chrome&ie=UTF-8', headers=headers)
  
    soup = BeautifulSoup(res.text, 'html.parser')

    stock_value = ""
    stock_value += soup.find("div", class_="PyJv1b").get_text()
    stock_value += '\t'
    stock_value += soup.find("div", class_="wx62f").get_text()
    stock_value += '\n'
    stock_value += soup.find("span", jsname="vWLAgc").get_text()
    stock_value += soup.find("span", jsname="T3Us2d").get_text()
    stock_value += '\n'
    stock_value += soup.find("span", jsname="lb3Vg").get_text()
    stock_value += soup.find("span", jsname="ihIZgd").get_text()
    stock_value += '\nClose Price: '
    stock_value += soup.find("span", jsname="wurNO").get_text()
    stock_value += ' '
    stock_value += soup.find("span", jsname="TmYleb").get_text()
    stock_value += ' '
    stock_value += soup.find("span", jsname="sam3Lb").get_text()

    print(stock_value)

    table_value = dict(zip([attribute.get_text() for attribute in soup.find_all("td", class_="JgXcPd")],
                        [value.get_text() for value in soup.find_all("td", class_="iyjjgb")]))

    for k, v in table_value.items():
        print(k, v)

code = input("Enter the stock code: ")

stock(code)