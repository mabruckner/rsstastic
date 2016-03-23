# rsstastic


An extremely simple rss server, with file-based storage and a modular design.

to run you need to create two empty files in this directory: read.csv and items.csv.
You also need to create a configuration file called config.json

here is an example

```
{
    "xkcd_rss":{
        "type":"rss",
        "config":"http://xkcd.com/rss.xml"
    },
    "xkcd_atom":{
        "type":"atom",
        "config":"http://xkcd.com/atom.xml"
    }
}
```
