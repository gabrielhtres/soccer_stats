import requests
from bs4 import BeautifulSoup

url = 'https://www.fotmob.com/pt-BR/players/263937'

# headers = {
#     'Accept': 'application/json,text/javascript,*/*; q=0.01',
#     'Accept-Encoding': 'gzip,deflate,br,zstd',
#     'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cookie': '_fbp=fb.1.1744377232150.90081823956029913;ct=BR; usprivacy=1N--;_gid=GA1.2.1184005572.1744377236;_xpid=5700294162;_xpkey=K42X62Ip7JVx3zHw2qRVBCnrixLWJCic;__cf_bm=rGeSLVZSEDkNZmUdQ4ja_7pFI5.UEjddC.zkcZavJRI-1744398387-1.0.1.1-OS4sGrR3n6GUPoQaWkrPU7qdbPFtqgpAmHcEhxuD52Qy7Drv8WNoHbLwUfUSqAlpohIdRyEzB8vn1IXjve0VtzJJj9d46wqIt4CgGqWucRWNeuNoRk2t1ok1h4kZLjGG;_gat_UA-6065109-1=1;_ga=GA1.2.421210813.1744377236;_ga_16TFZ6BTNV=GS1.1.1744398983.2.1.1744399979.58.0.0',
#     'Model-Last-Mode': 'xFMBT9i34v+W3nZoYUocS+Z+BN8+D88crAPotnmbJrY=',
#     'Priority': 'u=1,i',
#     'Referer': 'https://1xbet.whoscored.com/players/397517',
#     'Sec-Ch-Ua': '"Google Chrome";v="135","Not-A.Brand";v="8","Chromium";v="135"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'PostmanRuntime/7.28.4',
#     'X-Requested-With': 'XMLHttpRequest'
# }

# Faz a requisição para a página
response = requests.get(url)#, headers=headers)

if response.status_code == 200:
    html = response.text
    # Cria o objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    stats = soup.find_all('div', class_='e1uibvo10')
    image = soup.find_all('img', class_='Image PlayerImage ImageWithFallback')
    print('image', image[0]['src'])

    for index, s in enumerate(stats):
        text = s.get_text()
        print(text.split('Gols'))
        print('index', index)
        # print(s.get_text())
else:
    print(f"Erro: {response.status_code}")