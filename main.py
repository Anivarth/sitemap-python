import xmltodict, json, requests
from pprint import pprint

website_url = 'http://radiusofcircle.blogspot.com/sitemap.xml'

content = requests.get(website_url)

#Read all the data from the content
website_text = content.text

#Using the xmltodict to get the dict as string
webJson = json.dumps(xmltodict.parse(website_text))

urlset = json.loads(webJson)


urls = urlset['urlset']['url']

print(len(urls))
for element in urls:
    url = element['loc']
    r = requests.get(url)
    for line in r.iter_lines():
        if '<title>' in line:
            line = line.strip()
            print '<a href="'+url+'" >'+line[7:-8]+'</a><br /><br />\n'

