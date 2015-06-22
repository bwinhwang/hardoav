#!/usr/bin/env python
# encoding: utf-8
import argparse
import os
import os.path
import traceback
from multiprocessing.dummy import Pool as ThreadPool

import config

from filedown import FileDown
from caoliu import CaoLiu
__VERSION__ = "0.0.1"
def main():
    description = "set some options for hardoav"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-D", "--dir", dest="output_dir",
            default=config.OUTPUT_DIR, help="set directory for downloaded videos.")
    parser.add_argument("-W", "--worker_count", dest="worker_count", type=int,
            default=config.WORKER_COUNT,
            help="set worker count for simultaneously download a video")
    parser.add_argument("-S", "--site", dest="site", default=config.SITE,
            help="set site for scanning video urls")
    parser.add_argument("-T", "--topic_num", dest="topic_num", default=config.TOPIC_NUM,
            type=int, help="set scanning topic num")
    version = "%(prog)s " +  __VERSION__
    parser.add_argument("-V", "--version", action='version',
            version=version, help="show version number")

    args = parser.parse_args()
    output_dir = args.output_dir
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    site = args.site
    if not site.endswith("/"):
        site = site + '/'
    worker_count = args.worker_count
    if worker_count > 16 or worker_count < 1:
        worker_count = config.WORKER_COUNT
    topic_num = args.topic_num
    if topic_num < 1:
        topic_num = config.TOPIC_NUM

    pool=ThreadPool(worker_count)
    caoliu = CaoLiu(site, topic_num)
    for download_info in caoliu.gen_download_infos():
        file_url = download_info["file"]
        title = download_info["title"]
        print(file_url)
        filename = title + '.' + file_url.rsplit('.', 1)[1]
        try:
            print(file_url)
            print(title)
            fd = FileDown(filename, download_info["file"], worker_count, output_dir, download_info)
            fd.start(pool)
        except Exception as e:
            traceback.print_exc()



if __name__ == "__main__":
    main()


