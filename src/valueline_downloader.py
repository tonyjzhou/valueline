#!/usr/bin/env python3

import multiprocessing
import os
import time
from multiprocessing.dummy import Pool
from urllib.error import HTTPError
from urllib.request import urlretrieve


def all_file_names():
    return ["f%04d.pdf" % i for i in range(1, 10000)]


def retrieve(remote_dir, local_dir):
    def urlretrieve_safe(file_name):
        nonlocal remote_dir, local_dir

        os.makedirs(local_dir, mode=0o777, exist_ok=True)

        remote_url = remote_dir + file_name
        local_file = os.path.join(local_dir, file_name)
        try:
            urlretrieve(remote_url, local_file)
        except HTTPError:
            print("Cannot find %s" % remote_url)

    return urlretrieve_safe


def user_input():
    default_remote_dir = "http://www3.valueline.com/dow30/"
    default_local_dir = "/Users/tonyzhou/Google Drive/Investment/Valueline/dow30/"
    remote_dir = input("Enter remote dir (default '%s'):" % default_remote_dir) or default_remote_dir
    local_dir = input("Enter local dir (default '%s'):" % default_local_dir) or default_local_dir

    return remote_dir, local_dir


def main():
    remote_dir, local_dir = user_input()
    size = multiprocessing.cpu_count() * 2

    print("Going to download all files in '%s' to '%s' with %d threads" % (remote_dir, local_dir, size))
    input("Press Enter to continue...")

    start = time.time()
    Pool(size).map(retrieve(remote_dir, local_dir), all_file_names())
    end = time.time()

    print("Total threads = ", size)
    print("Total time = %f seconds" % (end - start))


if __name__ == "__main__":
    main()
