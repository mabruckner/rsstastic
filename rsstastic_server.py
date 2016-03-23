from bottle import route,run,template,get,abort,redirect
import csv
import json
import rsstastic
import base64
import util

config = {}
config_file = 'config.json'
with open(config_file,'r') as cfile :
    config = json.load(cfile)

items_file = 'items.csv'
read_file = 'read.csv'

def get_items() :
    with open(items_file,'r') as f :
        reader = csv.reader(f)
        output = {}
        for row in reader:
            output[row[0]] = (int(float(row[1])),row[2])
        return output

def get_read() :
    with open(read_file,'r') as f :
        reader = csv.reader(f)
        output = []
        for row in reader :
            output.append(row[0])
        return output

def add_items(items) :
    with open(items_file,'a') as f :
        writer = csv.writer(f)
        for itemid in items :
            item = items[itemid]
            writer.writerow([itemid,item[0],item[1]])

def add_read(read) :
    with open(read_file,'a') as f :
        writer = csv.writer(f)
        for thing in read :
            writer.writerow([thing])

def get_reader(config) :
    return rsstastic.Aggregator(config)

def update_items(reader):
    items = get_items()
    new_items = reader.get_items()
    really_new_items = {}
    for k,v in new_items.items() :
        if k not in items :
            really_new_items[k] = v
    add_items(really_new_items)

@get('/')
def index():
    items = get_items()
    have_read = get_read()
    read = []
    unread = []
    for x in items :
        val = {'id':x,'timestamp':items[x][0],'data':items[x][1]}
        if x in have_read :
            read.append(val)
        else :
            unread.append(val)
    read.sort(key=lambda x : -x['timestamp'])
    unread.sort(key=lambda x : -x['timestamp'])

    return template('templates/index.tpl', read=read, unread=unread)

@get('/item/<name>')
def item(name):
    realid = util.b64_to_key(name)
    items = get_items()
    if realid in items :
        read = get_read()
        if realid not in read :
            add_read([realid])
        data = get_reader(config).retrieve(realid,items[realid])
        keys = list(items.keys())
        keys.sort(key=lambda x: items[x][0])
        index = keys.index(realid)
        next = None if index+1 == len(keys) else keys[index+1]
        prev = keys[index-1]
        return template(
                'templates/item.tpl',
                data=data,
                itemid=realid,
                timestamp=items[realid][0],
                next=next,
                prev=prev)
    abort(404,"unable to find item")

def reload_config() :
    global config
    with open(config_file,'r') as cfile :
        config = json.load(cfile)
    update_items(get_reader(config))

@get('/reload')
def reload() :
    reload_config()
    redirect('/')

if __name__ == '__main__' :
    import atom
    import rss
    reload_config()
    run(host='localhost',port=5000)
