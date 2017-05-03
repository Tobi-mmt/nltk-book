# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 20 website extraction
# -----------------
import nltk, re
from urllib import request
import lxml.html

url = "http://at.wetter.com/oesterreich/salzburg/ATAT30532.html"
response = request.urlopen(url)
raw = response.read().decode('utf8')
page = lxml.html.document_fromstring(str(raw))
temperature = page.xpath("//div[@class='text--white beta palm-hide']")[0].text

print('In Salzburg hat es derzeit {}.'.format(temperature))
