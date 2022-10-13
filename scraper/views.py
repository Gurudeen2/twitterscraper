from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
from .models import twttb



def scraperfunc(request):
    # print('Yusuf',request.POST.get('tweetno'))
    twttb.objects.all().delete()
    if request.method == 'POST':
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        tweetno = request.POST.get('tweetno')
        text = request.POST['text']
    #get data from the url
        
        for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(
                f'{text} since:{startdate} until:{enddate}').get_items()):
            if i > int(tweetno):
                break
            twtsave = twttb.objects.create(username=tweet.user.username, content=tweet.content, language=tweet.lang,
            url=tweet.url, source=tweet.source)
            twtsave.save()


        
    context ={
        'twitter': twttb.objects.all()
    }
       
# https://twitter.com/search?f=live&lang=en&q=crytocurrency
    # twtcontent = requests.get('https://twitter.com/search?q=cyberakeem')


    return render(request, 'form.html', context  )








# class Crawler:

#     def __init__(self, urls=[]):
#         self.visited_urls = []
#         self.urls_to_visit = urls

#     def download_url(self, url):
#         return requests.get(url).text

#     def get_linked_urls(self, url, html):
#         soup = BeautifulSoup(html, 'html.parser')
#         for link in soup.find_all('a'):
#             path = link.get('href')
#             if path and path.startswith('/'):
#                 path = urljoin(url, path)
#             yield path

#     def add_url_to_visit(self, url):
#         if url not in self.visited_urls and url not in self.urls_to_visit:
#             self.urls_to_visit.append(url)

#     def crawl(self, url):
#         html = self.download_url(url)
#         for url in self.get_linked_urls(url, html):
#             self.add_url_to_visit(url)

#     def run(self):
#         while self.urls_to_visit:
#             url = self.urls_to_visit.pop(0)
#             logging.info(f'Crawling: {url}')
#             try:
#                 self.crawl(url)
#             except Exception:
#                 logging.exception(f'Failed to crawl: {url}')
#             finally:
#                 self.visited_urls.append(url)

# if __name__ == '__main__':
#     Crawler(urls=['https://www.imdb.com/']).run()