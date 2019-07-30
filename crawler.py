# -*- coding: utf-8 -*-
import requests
import lxml.html


class TvCrawler:
    def __init__(self):
        self.endpoint = 'https://tv.yahoo.co.jp'
        self.programs = {}

    def get_programs(self, word, date):
        params = {
            'q': word,
            'd': date
        }
        res = requests.get(self.endpoint + '/search', params=params)

        # TODO エラー処理
        html = lxml.html.fromstring(res.text)
        # TODO 0件だったときの処理
        for program in html.xpath('//*[@id="main"]/div[7]/ul/li'):
            title = program.xpath('div[2]/p[1]/a')[0].text
            content = program.xpath('div[2]/p[3]')[0].text
            if word not in title and word not in content:
                continue
            href = program.xpath('div[2]/p[1]/a/@href')[0]
            self.programs[title] = {
                'href': self.endpoint + href
            }


def main():
    target_date = '20190730'
    tv_crawler = TvCrawler()
    tv_crawler.get_programs('フランス', target_date)
    print(tv_crawler.programs)


if __name__ == '__main__':
    main()
