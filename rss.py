import requests
from lxml import etree
import time
import dateutil.parser
import rsstastic

class RssReader() :
    def __init__(self,config) :
        self.url = config
    def get_items(self) :
        response = requests.get(self.url)
        tree = etree.fromstring(response.content)
        root = tree.find('channel')
        items = {}
        for item in root.findall('item') :
            guid = item.find('guid').text
            summary = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
            if summary is None :
                summary = item.find('description').text
            else :
                summary = summary.text
            pubDate = item.find('pubDate')
            updated = int(time.time())
            if pubDate is not None:
                updated = int(dateutil.parser.parse(item.find('pubDate').text).timestamp())
            items[guid] = (updated,summary)
        return items
    def retrieve(self,key,item) :
        return item[1]

rsstastic.readermap['rss'] = RssReader

if __name__ == "__main__" :
    x = RssReader("http://xkcd.com/rss.xml")
    print(x.get_items())

