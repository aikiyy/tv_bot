# -*- coding: utf-8 -*-
from slacker import Slacker
from crawler import TvCrawler
import os
from optparse import OptionParser
from datetime import datetime


def make_message(word, date, programs):
    message = datetime.strptime(date, '%Y%m%d').strftime('%Y/%m/%d') + '   ' + word + '\n'
    for title, v in programs.items():
        message += v['time'] + '   ' + v['genre1'] + ' - ' + v['genre2'] + '\n'
        message += '       <' + v['href'] + '|' + title + '>' + '\n'
    message += '- - - - - - - - - - - - - - - - - - - - - - - - -'
    return message


def post_slack(options):
    try:
        slack_token = os.environ['SLACK_TOKEN']
    except KeyError:
        raise KeyError('環境変数SLACK_TOKENが設定されていません.')

    try:
        channel = os.environ['POST_CHANNEL']
    except KeyError:
        channel = 'bot_test'

    try:
        icon_emoji = os.environ['ICON_EMOJI']
    except KeyError:
        icon_emoji = ':tv:'

    slack = Slacker(slack_token)
    tv_crawler = TvCrawler()
    tv_crawler.get_programs(options.word, options.date)

    message = make_message(options.word, options.date, tv_crawler.programs)
    slack.chat.post_message(channel, message, icon_emoji=icon_emoji)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-w', '--word', dest='word', type='string')
    parser.add_option('-d', '--date', dest='date', type='string')
    (options, args) = parser.parse_args()
    post_slack(options)
