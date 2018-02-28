#!/usr/bin/env python
# encoding: utf-8

import sqlite3
import config
import traceback
import os

class DB:

  def __init__(self,dbfile = config.SQLITE_FILE ):

    self.dbfile = dbfile
    if not os.path.exists(dbfile):
      conn = sqlite3.connect(self.dbfile)
      c = conn.cursor()
      c.execute('CREATE TABLE {tn} (url TEXT NOT NULL UNIQUE PRIMARY KEY, \
      title TEXT, \
      file TEXT,\
      size INTEGER,\
      length INTEGER)',config.SQLITE_TABLE)
      c.close()
      conn.commit()
      conn.close()

  def insert_video_item(self,url,title,file='',size = 0,length = 0):
    conn = sqlite3.connect(self.dbfile)
    c = conn.cursor()
    try:
      c.execute('SELECT * FROM {tn} WHERE url = ? ',(config.SQLITE_TABLE,url,))
      data = c.fetchone()
      if data is None:
        c.execute('INSERT INTO ? values(?,?,?,?,?)',
                  (config.SQLITE_TABLE, url,title,file,size,length,))
        c.close()
        conn.commit()
        conn.close()
        print "Insert %s " % (title)
    except Exception as _:
      traceback.print_exc()
    finally:
      c.close()
      conn.close()

  def insert_video_items(self,items):
    for item in items:
      self.insert_video_item(self,item.url, item.title, item.file, item.size, item.length)

  def update_video_item(self):
    pass


