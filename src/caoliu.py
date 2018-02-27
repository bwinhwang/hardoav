#!/usr/bin/env python
# encoding: utf-8

import json
import traceback
import re
import os.path
import sys



import requests
import bs4

AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
CHUNK_SITE = 1024 * 32

def find_download_info(session, url):
    # site1 = "http://up2stream.com"
    # site2 = "http://ppt.cc"
    r = session.get(url)
    # print(r.request.headers)
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
    PATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-&\--_*+@.]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    file_urls = re.findall(PATTERN, content)
    print(file_urls)
    # print(content)
    # soup = bs4.BeautifulSoup(r.text, "lxml")
    file_url = None
    # ret = re.search(r"eval\(.*\)", content)
    # js = ret.group()
    # file_url = up2stream(js)
    # file_url = pptcc(js)
    # now use regular expression to find file url.
    try:
        for fu in file_urls:
            # fu = fu.rstrip('/')
            no_query_fu = fu.split('?', 1)[0]
            if no_query_fu.rsplit('.')[-1] in ('mp4', 'mp4/'):
                file_url = fu
                break
    except Exception as e:
        print(e)
        print("Can't handle url", src)

    if file_url:
    	return dict(file=file_url, Referer=src, title=title)
    else:
    	return None

def pptcc(js):
    import execjs
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
    import execjs
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
    if not file_url or "36abc039c05dff6d1a82e0c7988c467d" in file_url:
        return None
    return file_url


class CaoLiu(object):
    def __init__(self, site, topic_num, output_dir, url=None, type=1):
        self.site = site
        self.topic_num = topic_num
        self.url = url # individual topic url
        self.type = type # 1 for Asian NoMosaic, 2 for Asian Mosaic
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers["User-Agent"] = AGENT

    def _get_topic_url(self):
        thread_url = self.site + "thread0806.php?fid=22&search=&type=${type}&page={page}"
        page = 1
        scanned_topic = 0
        while True:
            topic_urls = []
            url = thread_url.format(type=type,page=page)
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
                    print(scanned_topic)
                    print(title)
                    topic_urls.append(href)
                    # print(u"title: %s\nurl: %s" % (title, href))
                    scanned_topic += 1
                    if scanned_topic >= self.topic_num
                        break
                except Exception as _:
                    traceback.print_exc()
            print("scaned topic_num: %d" % scanned_topic)
            if scanned_topic >= self.topic_num:
                break
            page += 1
        return topic_urls

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
            for topic_urls in self._get_topic_url():
                pass

    def download(self, download_info, filename):
        headers = dict(Referer=download_info["Referer"])
        headers["User-Agent"] = AGENT

        filename = os.path.join(self.output_dir, filename)
        local_size = 0
        if os.path.isfile(filename):
            local_size = os.path.getsize(filename)
            headers["Range"] = "bytes=%d-" % local_size
            print("resume download at bytes: %d" % local_size)

        # self.session.get("http://adv.up2stream.com/adsprp.php", headers=headers)
        r = self.session.head(download_info["file"], headers=headers, allow_redirects=True)
        # print("status_code", r.status_code)
        print(r.headers)
        print(r.request.url)
        print(r.url)
        r = self.session.get(download_info["file"], headers=headers, stream=True)
        try:
            content_length = int(r.headers["Content-Length"])
        except Exception as e:
            r = self.session.get(download_info["file"], headers=headers)
            content_length = int(r.headers["Content-Length"])
        content_length += local_size
        if local_size == content_length or r.status_code == 416:
            print("already downloaded, skip it.")
            return None
        print("start downloading...")
        content_length_mb = content_length / 2**20
        with open(filename, "ab") as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SITE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                local_size += len(chunk)
                process_bar = "#"*int(local_size * 50 / content_length)
                process_bar += str(local_size / 2**20) + "MB/"
                process_bar += str(content_length_mb) + "MB"
                sys.stdout.write('\r'+ process_bar)
                sys.stdout.flush()
            sys.stdout.write('\n')
        print("saved to " + filename)
        return True
