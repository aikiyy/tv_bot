# -*- coding: utf-8 -*-
import requests
import lxml.html


class TvCrawler:
    def __init__(self):
        self.endpoint = 'https://tv.yahoo.co.jp'
        self.programs = {}

    def get_programs(self, word, date, exwords=None):
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

            _f = False
            for exword in exwords.split(','):
                if exword in title or exword in content:
                    _f = True
            if _f:
                continue

            href = program.xpath('div[2]/p[1]/a/@href')[0]
            time = program.xpath('div[1]/p[2]/em')[0].text
            genre1 = program.xpath('div[2]/p[2]/span/a[1]')[0].text
            genre2 = program.xpath('div[2]/p[2]/span/a[2]')[0].text
            self.programs[title] = {
                'href': self.endpoint + href,
                'time': time,
                'genre1': genre1,
                'genre2': genre2
            }


def main():
    tv_crawler = TvCrawler()
    tv_crawler.get_programs('フランス', '20190730', 'フランス語')
    print(tv_crawler.programs)


if __name__ == '__main__':
    main()
