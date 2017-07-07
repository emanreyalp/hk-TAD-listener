import urllib2
import re

def remove_comments(raw_html):
    return re.sub(r"<!--.*-->", "", raw_html, flags=re.DOTALL)

with open('TADs') as TADs_file:
    TADs = TADs_file.readlines()

link = "http://portal.vik.bme.hu/kepzes/targyak/%s/" % TADs[0]
f = urllib2.urlopen(link)
myfile = f.read()
myfile2 = remove_comments(myfile)

print(myfile2)
