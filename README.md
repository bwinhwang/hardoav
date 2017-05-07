hardoav
=======
A Simple tool for you download oav at caoliu



Usage
=====
```bash
usage: hardoav.py [-h] [-D OUTPUT_DIR] [-W WORKER_COUNT] [-S SITE] [-U URL]
                  [-T TOPIC_NUM] [-V]

set some options for hardoav

optional arguments:
  -h, --help            show this help message and exit
  -D OUTPUT_DIR, --dir OUTPUT_DIR
                        set directory for downloaded videos.
  -W WORKER_COUNT, --worker_count WORKER_COUNT
                        set worker count for simultaneously download a video
  -S SITE, --site SITE  set site for scanning video urls
  -U URL, --url URL     set individual url to download
  -T TOPIC_NUM, --topic_num TOPIC_NUM
                        set scanning topic num
  -V, --version         show version number
```

Requirement
===========
* requests
* ~~PyExecJS~~
* ~~jsbeautifier~~


TODO
====
* support range download, continue download when partial downloaded, not skip it
* ~~support socks5, http proxy~~ use proxychain
* ~~maybe change to C++~~ too complex, not worth to port
* ~~maybe use requests to download~~ already implemented

Changelog
========
Version 0.0.3:
* use regular expression to find file url

Version 0.0.2:
* support major two sites in CaoLiu OAV
* use Requests to download, not use filedown.py
* add a process bar when downloading

LICENSE
=======
*JFLX*
