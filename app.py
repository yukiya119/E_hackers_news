import time

import requests

from search_news import search_news

# トップページに掲載されている30記事のidをとってくる。
top30id = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

# 30記事のidを入れる空の配列を定義。
top30url = []


def main():
    # 入力
    top = 5
    # 処理
    all_news = search_news(top=top)
    # 出力
    for news in all_news:
        print(news)


# 30記事のid情報が入った配列「top30id」を30回繰り返し、idに入れ、30個のurlを生成する。それを配列「top30url」に追加。
for id in top30id.json()[0:30]:
    top30url.append(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
for i in range(len(top30url)):
    # 各記事の情報を取得し、変数「response」に定義。
    response = requests.get(top30url[i])
    # 「'title'」の情報を変数「title」に定義。
    title = response.json()['title']
    # 「'url'」の情報を変数「url」に定義。
    url = response.json()['url']
    # 1秒待ってね。
    time.sleep(1)
    # 出力
    print(f"'title': {title}, 'link': {url}")
if __name__ == '__main__':
    main()
