import json

readermap = {}

class DummyReader() :
    def __init__(self,config) :
        pass
    def get_items(self) :
        return {}
    def retrieve(self,item) :
        return "NOTHING"

readermap["dummy"] = DummyReader

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
        for name in self.readers :
            reader = self.readers[name]
            for k,v in reader.get_items().items() :
                items[json.dumps([name,k])] = v
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

