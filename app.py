import time

import requests


def requests_top():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'  # New, Top and Best Stories
    response = requests.get(url)  # response = requests.get(URL, その他任意の引数)
    article = response.json()
    for i in article:
        time.sleep(1)  # sleepのタイミングを変更
        try:  # 例外処理(try-except構文)
            response2 = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty').json()
            if 'url' in response2:
                print('{ title:' + response2['title'], ', Link:' + response2['url'], '}')

        except KeyError:  # 辞書型データを参照した際に、辞書内に指定したキーが存在しないと、KeyErrorが発生
            pass  # try-except構文を用いて対処。passは何もしない文


def main():
    requests_top()


if __name__ == '__main__':
    main()
