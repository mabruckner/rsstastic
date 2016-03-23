import requests
from lxml import etree
import time
import dateutil.parser
import rsstastic
from io import BytesIO

class UpdateReader() :
    def __init__(self,config) :
        self.url = config['url']
        self.selector = config['selector']
    def get_items(self) :
        response = requests.get(self.url)
        parser = etree.HTMLParser()
        tree = etree.parse(BytesIO(response.content),parser)
        thing = tree.getroot().cssselect(self.selector)[0]
        return {thing.get('src'):(time.time(),'')}
    def retrieve(self,key,item) :
        return '<img src="{}"></img>'.format(key)

rsstastic.readermap['update'] = UpdateReader

