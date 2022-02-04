import time

import requests


def requests_top():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'  # New, Top and Best Stories
    response = requests.get(url)  # response = requests.get(URL, その他任意の引数)
    list = response.json()
    for i in list:
        try:
            response2 = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty').json()
            print('{ title:' + response2['title'], ', Link:' + response2['url'], '}')
            time.sleep(1)
        except KeyError:
            pass


def main():
    requests_top()


if __name__ == '__main__':
    main()
