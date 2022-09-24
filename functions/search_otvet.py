import requests
import fake_useragent
from bs4 import BeautifulSoup


def searchotvet(query): #функия поиска ответа в интренете
    # query = query
    query = query.replace(' ', '+')
    url = f'https://go.mail.ru/search?q={query}'
    user = fake_useragent.UserAgent().random
    headers = {
    'user-agent': user
    }
    resp = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')
    results = soup.find_all('ul', class_="result js-result")
    list_result = []
    for result in results:
        link = result.find_all('a', class_="light-link")
        k = 0
        for i in link:
            if k == 5:
                return list_result
            else:
                link1 = i['href']
                list_result.append(link1)
                k += 1
    return list_result
