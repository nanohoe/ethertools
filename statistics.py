#!/usr/bin/python

import re
from datetime import datetime as dt
import urllib2

def main():
    url = 'http://dwarfpool.com/eth/address?wallet=<your_wallet_address'
    s = urllib2.urlopen(url).read()
    
    tablestart = s.find(b"Shares for last 24 hours")
    tablestart = s.find(b"<tbody>", tablestart+1)
    tableend = s.find(b"</tbody>", tablestart) + 8
    
    data = re.sub('<.*?>', ' ', s[tablestart:tableend])
    data = re.sub('\(.*?\)', '', data)
    
    intermediate = data.split(b"\n")
    datalist = [];
    
    for d in intermediate[1:-1]:
        #print(d.split(b" ")[-3])
        d2 = d.replace(b",", b"").split()
        if len(d2) == 6:
            print(b" ".join(d2[:-1]))
        
#    print(intermediate)
    
if __name__ == '__main__':
    main()
