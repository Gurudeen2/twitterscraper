from cgitb import html
import requests
from bs4 import BeautifulSoup
import snscrape.modules.twitter as sntwitter

param = '' 
twtcontent = requests.get('https://twitter.com/search?q=cyberakeem')
# twtcontent = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
htmlpaser = BeautifulSoup(twtcontent.content, 'lxml')
mainsel = htmlpaser.select('div')
# print('twitter  =', twtcontent.text)
# tt= htmlpaser.title.text

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(
            'crytocurrency since:2022-01-01 until:2022-08-13').get_items()):
    if i > 10:
        break
    #2 save data automatically to the HarperB cloud instance
    data = {
        "user_name": tweet.user.username,
        "content": tweet.content,
        "lang": tweet.lang,
        "url": tweet.url,
        "source": tweet.source
    }

    with open('log.txt', 'a') as f:
        f.write(str(tweet.user.username))
        f.write('\n')
# print('twitter Text  =', twtcontent.text)