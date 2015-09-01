#!/usr/bin/env python
# encoding: utf-8

import json
import traceback



import requests
import bs4

AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36'

def find_download_info(session, url):
    site1 = "http://up2stream.com"
    site2 = "http://videowood.tv/embed"
    r = session.get(url)
    r.encoding = "gb2312"
    soup = bs4.BeautifulSoup(r.text, "lxml")
    title = unicode(soup.find("title").string).rsplit(']', 1)[0] + ']'
    embed = soup.find("embed")
    src = embed.get("src")
    if not src.startswith((site1, site2)):
        return None
    headers = dict(Referer=url)
    r = session.get(src, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    if src.startswith(site2):
    	file_url = videowood(soup)
    else:
    	file_url = up2stream(soup)
    if file_url:
    	return dict(file=file_url, Referer=src, title=title)
    else:
    	return None

def videowood(soup):
    scripts = soup.find_all("script")
    for script in scripts:
        script_text = unicode(script.string).strip()
        if "config" in script_text:
            tmp = script_text.split("file:", 1)[1].strip()
            file_url = tmp.split(",", 1)[0].strip("\"")
            return file_url

def up2stream(soup):
    video = soup.find("video", id="container")
    source = video.find("source")
    file_url = source.get("src")
    return file_url


class CaoLiu(object):
    def __init__(self, site, topic_num, url=None):
        self.site = site
        self.topic_num = topic_num
        self.url = url # individual topic url
        self.session = requests.Session()
        self.session.headers["User-Agent"] = AGENT

    def _get_topic_url(self):
        thread_url = self.site + "thread0806.php?fid=22&search=&page={page}"
        page = 1
        scanned_topic = 0
        topic_urls = []
        while True:
            url = thread_url.format(page=page)
            print (url)
            r = self.session.get(url)
            r.encoding = "gb2312"
            soup = bs4.BeautifulSoup(r.text, "lxml")
            table = soup.find("table", id="ajaxtable")
            h3s = table.find_all("h3")
            for h3 in h3s:
                a = h3.find("a")
                try:
                    href = self.site + a.get("href")
                    title = unicode(a.string).replace(" ", "")
                    topic_urls.append(href)
                    scanned_topic += 1
                except Exception as e:
                    traceback.print_exc()
            print scanned_topic
            if scanned_topic >= self.topic_num:
                break
            page += 1
        return topic_urls

    def gen_download_infos(self):
        topic_urls = []
        if not self.url:
            # scan
            topic_urls.extend(self._get_topic_url())
        else:
            # individual url download
            topic_urls.append(self.url)
        for i, url in enumerate(topic_urls, start=1):
            if i >= self.topic_num:
                break
            download_info = None
            try:
                download_info = find_download_info(self.session, url)
            except Exception as e:
                traceback.print_exc()
            if download_info:
                yield download_info

