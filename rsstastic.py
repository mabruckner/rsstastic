import json
import traceback
from multiprocessing import Pool, cpu_count

readermap = {}

class DummyReader() :
    def __init__(self,config) :
        pass
    def get_items(self) :
        return {}
    def retrieve(self,item) :
        return "NOTHING"

readermap["dummy"] = DummyReader

def get_items_named(tpl):
    (name,reader) = tpl
    print("fetching ", name)
    try:
        items = []
        for k,v in reader.get_items().items():
            items.append((json.dumps([name,k]),v))
        return items
    except Exception as e:
        traceback.print_exc()
        return []

class Aggregator() :
    def __init__(self,config) :
        self.readers = {}
        for name in config :
            rconf = config[name]
            rtype = readermap.get(rconf["type"],DummyReader)
            reader = rtype(rconf["config"])
            self.readers[name] = reader
    def get_items(self) :
        items = {}
        pool = Pool(cpu_count()*2)
        found = pool.map(get_items_named, [(name, self.readers[name]) for name in self.readers])
        for group in found:
            for (k, v) in group:
                items[k] = v
        return items
    def retrieve(self,key,data) :
        dat = json.loads(key)
        reader = self.readers[dat[0]]
        return reader.retrieve(dat[1],data)

readermap["aggregator"] = Aggregator

def update_readers(config) :
    for name in config["readers"] :
        rconf = config["readers"][name]
        rtype = readermap.get(rconf["type"],DummyReader)
        reader = rtype(rconf["config"])
        items = Reader

