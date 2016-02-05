#!/usr/bin/env python2
#!---coding:utf-8---
import os
import sys
import tempfile
import urllib2


AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
CHUNK_SIZE = 4096

class FileDown(object):
    def __init__(self, filename, url, worker_count, output_dir, info):
        req=urllib2.Request(url)
        req.headers['user-agent']=AGENT
        req.headers["referer"] = info["Referer"]
        f_headers=urllib2.urlopen(req)
        self.headers=f_headers.headers

        self.size=int(self.headers['content-length'])
        f_headers.close()
        self.part_size=self.size/worker_count
        self.range=range(0,self.size+1,self.part_size)
        self.range[-1]=self.size+1
        self.name=filename
        self.url=url
        self.output_dir = output_dir
        self.info = info
        self.partsfiles={}

    def start(self, pool):
        filename = os.path.join(self.output_dir, self.name)
        if os.path.isfile(filename):
            return
        print ("starting download...")
        pool.map(self.rangeDown,range(len(self.range)-1))
        print ("merge files...")
        self.merge()
        print ("cleaning...")
        self.clean()


    def rangeDown(self,index):
        prefix, suffix = self.name.rsplit('.', 1)
        suffix = '.' + suffix
        write_fd,tempname=tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=self.output_dir)
        print(tempname)
        self.partsfiles[index]=tempname
        downed=0
        total=self.range[index+1]-self.range[index]

        req=urllib2.Request(self.url)
        req.headers['User-Agent']=AGENT
        req.headers['Range']='bytes=%s-%s' %(self.range[index],self.range[index+1]-1)
        req.headers["referer"] = self.info["Referer"]
        f=urllib2.urlopen(req)
        while True:
            chunk_data=f.read(CHUNK_SIZE)
            if not chunk_data:
                f.close()
                os.close(write_fd)
                break
            os.write(write_fd,chunk_data)
            downed+=len(chunk_data)
    def merge(self):

        filename = os.path.join(self.output_dir, self.name)
        with open(filename, "wb") as writef:
            for i in range(len(self.range)-1):
                with open(self.partsfiles[i],"rb") as readf:
                    while True:
                        data = readf.read(CHUNK_SIZE)
                        if not data:
                            break
                        writef.write(data)
            print("successfully downloaded")

    def clean(self):
        for i in range(len(self.range)-1):
            os.remove(self.partsfiles[i])



def chunk_read(rf):
    yield readf.read(CHUNK_SIZE)
