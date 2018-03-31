# !/usr/bin/python
# coding=utf-8
import requests, glob, time, random
from urlparse import urlparse
import os, sys
from multiprocessing import Pool
import codecs
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
rr = '\033[39m'


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])



def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """



                White Hat Hackers
           _____       _ _    __ _           _           
          / ____|     | (_)  / _(_)         | |          
         | (___   __ _| |_  | |_ _ _ __   __| | ___ _ __ 
          \___ \ / _` | | | |  _| | '_ \ / _` |/ _ \ '__|
          ____) | (_| | | | | | | | | | | (_| |  __/ |   
         |_____/ \__, |_|_| |_| |_|_| |_|\__,_|\___|_|   
                    | |      Iran-cyber.Net                            
                    |_|          Github.com/04x     

 Note! : We don't Accept any responsibility for any illegal usage.       
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

try:
    with codecs.open('results/MyBeSqliVulnList.txt', mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    cls()
    print_logo()
    print r + '---------------------------------------------------------'
    print r + '    [' + y + '-' + r + '] ' + c + ' file MyBeSqliVulnList.txt Not Found! frist Run GetSqliTargets.py!!!'
    sys.exit()


ooo = list((ooo))


def get_url(url):
    try:
        error = ["DB Error", "SQL syntax;", "mysql_fetch_assoc", "mysql_fetch_array", "mysql_num_rows",
                 "is_writable",
                 "mysql_result", "pg_exec", "mysql_result", "mysql_num_rows", "mysql_query", "pg_query",
                 "System Error",
                 "io_error", "privilege_not_granted", "getimagesize", "preg_match", "mysqli_result", 'mysqli']

        if url.startswith("http://"):
            url = url.replace("http://", "")
        elif url.startswith("https://"):
            url = url.replace("https://", "")
        else:
            pass
        for s in error:
            Checksqli = requests.get('http://' + url + "'", timeout=5)

            if s in Checksqli.text.encode('utf-8'):
                SQLI = url.replace("'", "")
                break
        with open('results/SQLI_OK.txt', 'a') as xx:
            xx.write(SQLI + '\n')
        print c + '       [' + y + '+' + c + '] ' + g + url + g + ' [OK]'
    except:
        pass

def goo():
    try:
        pp = Pool(65)
        pp.map(get_url, ooo)
    except:
        pass


if __name__ == '__main__':
    cls()
    print_logo()
    print c + '       [' + y + '+' + c + '] ' + y + ' Scanning #'
    goo()

