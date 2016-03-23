import requests
from lxml import etree
import time
import dateutil.parser
import rsstastic

class AtomReader() :
    def __init__(self,config) :
        self.url = config
    def get_items(self) :
        namespace = "{http://www.w3.org/2005/Atom}"
        response = requests.get(self.url)
        tree = etree.fromstring(response.content)
        root = tree
        items = {}
        for item in root.findall(namespace+'entry') :
            atomid = item.find(namespace+'id').text
            summary = item.find(namespace+'summary').text
            updated = int(dateutil.parser.parse(item.find(namespace+'updated').text).timestamp())
            items[atomid] = (updated,summary)
        return items
    def retrieve(self,key,item) :
        return item[1]

rsstastic.readermap['atom'] = AtomReader

if __name__ == "__main__" :
    x = AtomReader("http://xkcd.com/atom.xml")
    print(x.get_items())

