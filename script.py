import requests, csv
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Pedro',
    'From': 'pedrobarcellosdosreis@gmail.com'
}

search_query = 'iphone'
page = requests.get("https://www.amazon.com.br/s?k=" + search_query +"", headers = headers)

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

results = soup.find_all("div", attrs={"class": "a-section a-spacing-medium"})

## Criar CSV
f = csv.writer(open("produtos.csv","w"))
f.writerow(["NOME","PREÇO"]) ## Cabeçalho

for r in results:

    name_span_list = r.find_all("a", attrs={"class": "a-link-normal a-text-normal"}) ## Seleciona e guarda os spans
    price_span_list = r.find_all("span", attrs={"class":"a-price"}) ## Seleciona e guarda os preços
    
    for name in name_span_list:
        name = name.span.text
        for price in price_span_list:
            price = price.span.text
            print(name+" , "+price) ## Exibe no console
            f.writerow([name,price]) ## Grava no arquivo CSV