#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crawling news numbers related to a singer
"""

# prepare workspace
import requests
from lxml import etree
import pandas as pd

if __name__ == '__main__':
	# get news from the different website
    url = 'http://news.baidu.com/ns'
	
	# the artists you want to search
    artist_name = ["甲壳虫乐队唱","叶倩文唱","周华健唱","SHE唱"]
	
	# date range
	#dates = ['20150301', '20150302']
    pred_date = pd.date_range('3/1/2015', periods = 244, freq="D")
	
	
	dates = [i.strftime("%Y%m%d") for i in pred_date]
	print dates
	
	# payload info
	payload = {'tn': 'news', 
               'rn': 20,
               'ie': 'utf-8', 
               'ct': 1,
               'word': ''}

   
    artist_day_news = {}
    for name in artist_name:
        artist_day_news[name] = {}
        for date in dates:
            artist_day_news[name][date] = -1
    print artist_day_news
    
    for name in artist_name:
        for date in dates:
            payload['word'] = name + date
            print payload['word'].decode('utf-8')
            try :
                html = requests.get(url, params=payload, timeout = 1)
                dom = etree.HTML(html.text)
                founds = dom.xpath("/html/body/div/div[@id='header_top_bar']/span/text()")
                #print type(num_news), len(num_news)
                print founds[0], len(founds[0]), founds[0][-2]
                #assert len(founds)  == 1
                num_news = int(founds[0][-2])
                artist_day_news[name][date] = num_news
            except:
                try :
                    html = requests.get(url, params=payload, timeout = 1)
                    dom = etree.HTML(html.text)
                    founds = dom.xpath("/html/body/div/div[@id='header_top_bar']/span/text()")
                    #print type(num_news), len(num_news)
                    print founds[0], len(founds[0]), founds[0][-2]
                    #assert len(founds)  == 1
                    num_news = int(founds[0][-2])
                    artist_day_news[name][date] = num_news
                except:
                    print "error"
                    artist_day_news[name][date] = 0
                    
            
    ### SAVE RESULTS   
    print artist_day_news
    f = open('artist_day_news.txt', 'w')
    for name in artist_name:
        for date in dates:
            f.write(name + ',')
            f.write(date + ',')
            f.write(str(artist_day_news[name][date]) + '\n')
    f.close()