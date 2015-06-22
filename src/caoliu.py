#!/usr/bin/env python
# encoding: utf-8

import json
import traceback



import requests
import bs4

AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36'

def find_download_info(session, url):
    r = session.get(url)
    r.encoding = "gb2312"
    soup = bs4.BeautifulSoup(r.text, "lxml")
    embed = soup.find("embed")
    src = embed.get("src")
    if not src.startswith("http://videowood.tv/embed"):
        return None
    headers = dict(Referer=url)
    r = session.get(src, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    scripts = soup.find_all("script")
    for script in scripts:
        script_text = unicode(script.string).strip()
        if "config" in script_text:
            print(script_text)
            try:
                tmp = script_text.split("file: \'", 1)[1].strip()
                file_url = tmp.split(",", 1)[0].strip("\'")
                if not file_url.startswith("http://"):
                    print(file_url)
                    continue
            except Exception as e:
                traceback.print_exc()
                continue
            c = dict(file=file_url)
            c["Referer"] = src
            return c
    return None



class CaoLiu(object):
    def __init__(self, site, topic_num):
        self.site = site
        self.topic_num = topic_num
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
                    topic_urls.append((href, title))
                    scanned_topic += 1
                except Exception as e:
                    traceback.print_exc()
            print scanned_topic
            print type(self.topic_num)
            if scanned_topic >= self.topic_num:
                break
            page += 1
        return topic_urls

    def gen_download_infos(self):
        topic_urls = self._get_topic_url()
        for i, topic in enumerate(topic_urls, start=1):
            if i >= self.topic_num:
                break
            url = topic[0]
            title = topic[1]
            try:
                download_info = find_download_info(self.session, url)
            except Exception as e:
                traceback.print_exc()
                download_info = None

            if download_info:
                download_info["title"] = title
                yield download_info

