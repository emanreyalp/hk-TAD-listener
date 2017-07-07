import urllib2

link = "http://portal.vik.bme.hu/kepzes/targyak/VIAUAC05/"
f = urllib2.urlopen(link)
myfile = f.read()

print(myfile)
