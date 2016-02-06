#!/usr/bin/env python
# encoding: utf-8

import json
import traceback
import re
import os.path
import sys



import requests
import bs4
import execjs

AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
CHUNK_SITE = 1024 * 32
NEXT_LINE = 2**20 / CHUNK_SITE

def find_download_info(session, url):
    site1 = "http://up2stream.com"
    site2 = "http://ppt.cc"
    r = session.get(url)
    print(r.request.headers)
    r.encoding = "gb2312"
    soup = bs4.BeautifulSoup(r.text, "lxml")
    title = unicode(soup.find("title").string).rsplit(']', 1)[0] + ']'
    div = soup.find("div", class_="tpc_content do_not_catch")
    print("*"*100)
    print(u"title: %s\nurl: %s" % (title, url))
    a = div.find_all("a")[1]
    onclick = a["onclick"]
    onclick = onclick.rsplit("'", 2)
    src = onclick[-2]
    print("iframe src: %s" % src)
    headers = dict(Referer=url)
    headers["User-Agent"] = AGENT
    r = session.get(src, headers=headers)
    content = r.content
    ret = re.search(r"eval\(.*\)", content)
    if not ret:
        return None
    js = ret.group()
    # soup = bs4.BeautifulSoup(r.text, "lxml")
    file_url = None
    if src.startswith(site1):
    	file_url = up2stream(js)
    elif src.startswith(site2):
        file_url = pptcc(js)
        # pass

    if file_url:
    	return dict(file=file_url, Referer=src, title=title)
    else:
    	return None

def pptcc(js):
    ret = execjs.eval(js)
    return ret["file"]

FAKE_JQUERY='''
function $(id) {
    function attr(src, url) {return url;}
    var o = {};
    o.attr = attr;
    return o;
}

'''

def up2stream(js):
    file_url = None
    ctx = execjs.compile(FAKE_JQUERY)
    try:
        file_url = ctx.eval(js)
    except execjs.ProgramError as e:
        # ReferenceError: DUNUfdcXVfY is not defined
        print(e)
        e = str(e)
        flag = e.split()[1]
        flag = "var %s=true;" % flag
        ctx = execjs.compile(FAKE_JQUERY + flag)
        file_url = ctx.eval(js)
    return file_url


class CaoLiu(object):
    def __init__(self, site, topic_num, output_dir, url=None):
        self.site = site
        self.topic_num = topic_num
        self.url = url # individual topic url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers["User-Agent"] = AGENT

    def _get_topic_url(self):
        thread_url = self.site + "thread0806.php?fid=22&search=&page={page}"
        page = 1
        scanned_topic = 0
        while True:
            topic_urls = []
            url = thread_url.format(page=page)
            print(url)
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
                    # print(u"title: %s\nurl: %s" % (title, href))
                    scanned_topic += 1
                except Exception as _:
                    traceback.print_exc()
            print("scaned topic_num: %d" % scanned_topic)
            page += 1
            yield topic_urls

    def start_scan(self):
        if self.url:
            # individual url download
            download_info = None
            try:
                download_info = find_download_info(self.session, self.url)
            except Exception as _:
                traceback.print_exc()
            if download_info:
                file_url = download_info["file"]
                title = download_info["title"]
                try:
                    print(file_url)
                    print(title)
                    filename = title + '.' + file_url.rsplit('?', 1)[0].rsplit('.', 1)[1]
                    self.download(download_info, filename)
                except Exception as _:
                    traceback.print_exc()
        else:
            # scan
            count = 1
            for topic_urls in self._get_topic_url():
                if count > self.topic_num:
                    break
                for url in topic_urls:
                    if count > self.topic_num:
                        break
                    download_info = None
                    try:
                        download_info = find_download_info(self.session, url)
                    except Exception as _:
                        traceback.print_exc()
                    if download_info:
                        file_url = download_info["file"]
                        title = download_info["title"]
                        try:
                            print("count is: %d" % count)
                            print(file_url)
                            print(title)
                            filename = title + '.' + file_url.rsplit('?', 1)[0].rsplit('.', 1)[1]
                            ret = self.download(download_info, filename)
                            if ret:
                                count += 1
                        except Exception as _:
                            traceback.print_exc()

    def download(self, download_info, filename):
        headers = dict(Referer=download_info["Referer"])
        headers["User-Agent"] = AGENT
        # self.session.get("http://adv.up2stream.com/adsprp.php", headers=headers)
        r = self.session.get(download_info["file"], headers=headers, stream=True)
        filename = os.path.join(self.output_dir, filename)
        if os.path.isfile(filename):
            print("already downloaded, skip it")
            return False

        print(r.headers)
        print("start downloading...")
        with open(filename, "wb") as f:
            for i, chunk in enumerate(r.iter_content(chunk_size=CHUNK_SITE), start=1):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                sys.stdout.write('\r'+ "#"*(i % NEXT_LINE) + str(i / NEXT_LINE) + "MB")
                sys.stdout.flush()
            sys.stdout.write('\n')
        print("saved to " + filename)
        return True
