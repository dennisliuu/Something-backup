import requests, feedparser, json
from bs4 import BeautifulSoup

class YahooFeed(object):
    def __init__(self, url='https://tw.news.yahoo.com/rss/'):
        self.url = url
        self.rss_feed = feedparser.parse(requests.get(url).text)

    def get_feedinfo(self):
        self.info = []
        for i, feed in enumerate(self.rss_feed['entries']):
            if i == 10:
                break
            
            title = feed['title']
            picture = feed['content'][0]['value']
            link = feed['link']
            self.info.append({'title': title, 'picture': picture, "link": link})
        return self.info

    def get_postcontext(self):
        #need sleep
        links = [link['link'] for link in self.info]

        self.context = []
        for link in links:
            #print(link)
            post = BeautifulSoup(requests.get(link).text, 'lxml')
            article = ""
            for line in post.find_all('p', href=False, class_=False):
                
                if len(post.find_all('p', )) == 1:
                    article = line.get_text()
                else:
                    if len(list(line.children)) == 1:
                        article += line.get_text()
            self.context.append(article)
        return self.context
    
    def pack_together(self):
        if len(self.info) == len(self.context):
            for info, context in zip(self.info, self.context):
                info['context'] = context
        else:
            print("content missing")
            return -1
        return self.info

if __name__ == "__main__":
    url = 'https://tw.news.yahoo.com/rss/'
    feed = YahooFeed(url)
    feed.get_feedinfo()
    feed.get_postcontext()
    data = feed.pack_together()
    print(data)

