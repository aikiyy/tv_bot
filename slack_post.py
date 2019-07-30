# -*- coding: utf-8 -*-
from slacker import Slacker
from crawler import TvCrawler
import os


def make_message(programs):
    message = ''
    for title in programs:
        message += '<' + programs[title]['href'] + '|' + title + '>' + '\n'
    return message


def main():
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
    tv_crawler.get_programs('フランス', '20190801')

    message = make_message(tv_crawler.programs)
    slack.chat.post_message(channel, message, icon_emoji=icon_emoji)


if __name__ == '__main__':
    main()
