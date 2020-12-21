import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    news_pieces = []
    soup = BeautifulSoup(html, features="html.parser")
    data_piece = soup.find('div', class_='Content').find('div', class_='NewsList Cont').find_all('div', class_='Item')
    for item in data_piece:
        header = item.find('h2').find('a').text
        date = item.find('div', class_='Date').text
        body = item.find_all('div')[-1].text
        news_pieces.append((date, header, body))
    return news_pieces


def save_news(news_list):
    with open('misc/news.txt', 'w', encoding='utf-8') as fout:
        for item in news_list:
            fout.write(f'{item[1]}\n{item[0]}\n{item[2]}\n\n')


def check_database(news_list):
    last_piece = News.query.last().heading
    print(news_list)
    checker = 0
    for i in news_list:
        if last_piece == i[1]:
            break
        else:
            checker += 1
        return checker



def save(news_list):
    with open('news.txt', 'w', encoding='utf-8') as fout:
        for item in news_list:
            fout.write(f'{item[1]}\n{item[0]}\n{item[2]}\n\n')

    return 'success'

def launch():
    url = 'http://www.turkmenskiy.ru/areanews/'
    html = get_html(url)
    data = get_data(html)
    save(data[:5])
    return data[:5]


def main():
    url = 'http://www.turkmenskiy.ru/areanews/'
    html = get_html(url)
    data = get_data(html)
    save(data[:5])


if __name__ == '__main__':
    main()
