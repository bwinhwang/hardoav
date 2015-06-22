hardoav
=======
A Simple tool for you download oav at caoliu



Usage
=====
```bash
usage: hardoav.py [-h] [-D OUTPUT_DIR] [-W WORKER_COUNT] [-S SITE]
                  [-T TOPIC_NUM] [-V]

set some options for hardoav

optional arguments:
  -h, --help            show this help message and exit
  -D OUTPUT_DIR, --dir OUTPUT_DIR
                        set directory for downloaded videos.
  -W WORKER_COUNT, --worker_count WORKER_COUNT
                        set worker count for simultaneously download a video
  -S SITE, --site SITE  set site for scanning video urls
  -T TOPIC_NUM, --topic_num TOPIC_NUM
                        set scanning topic num
  -V, --version         show version number
```

Requirement
===========
* requests


TODO
====
* support socks5, http proxy
* maybe change to C++
* maybe use requests to download


BUG
===
```
Traceback (most recent call last):
  File "hardoav.py", line 55, in main
    fd.start(pool)
  File "/root/hardoav/src/filedown.py", line 38, in start
    self.merge()
  File "/root/hardoav/src/filedown.py", line 71, in merge
    writef.write(readf.read())
MemoryError
```



LICENSE
=======
*JFLX*
