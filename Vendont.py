#!/usr/bin/env python """
from urllib.request import urlopen
import time
import json
import datetime
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

class color:
    HEADER = '\033[0m'
logo = color.HEADER + '''

   ██╗   ██╗███████╗███╗   ██╗██████╗  ██████╗ ███╗   ██╗████████╗
   ██║   ██║██╔════╝████╗  ██║██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝
   ██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║   ██║   
   ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║   ██║   
    ╚████╔╝ ███████╗██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║   ██║   
     ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝               
                          Author: @037
                          Version: 1.1

#######################################################################
| Vendont is a Venmo transaction finder/scraper. It uses Venmo's own  |
| public API system to fetch all transactions at a given time. This   |
| tool can be used to find Venmo usernames, real names, txid, and the |
| details of the receiving party in the transaction. This tool also   |
| includes the message enclosed within the transaction.               |
#######################################################################
'''
print(logo)
date_time = input('Enter the date where transactions begin [DD/MM/YYYY HH:mm:SS]: ') or datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
pattern = '%d/%m/%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
print('[*] Transformed "start" date to EPOCH: %s (local time zone)' %epoch)

date_time2 = input('Enter the date where transactions stop [DD.MM.YYYY HH:mm:SS]: ') or ((datetime.datetime.now() + datetime.timedelta(minutes = 1)).strftime('%d/%m/%Y %H:%M:%S'))
epoch2 = int(time.mktime(time.strptime(date_time2, pattern)))
print('[*] Transformed "end" date to EPOCH: %s (local time zone)' %epoch2)

limit = int(input('Enter the maximum amount transactions to collect (default/max is 20): ')) or 20
print('')
if(limit > 20):
    limit = 20
vjson = urlopen("https://venmo.com/api/v5/public?since=%s&until=%s&limit=%s" %(epoch, epoch2, limit))
obj = json.load(vjson)
#print(obj["data"])
i = 0
while i < limit and obj["data"][i] != None:
    if((obj["data"][i]["payment_id"] is not None) and (obj["data"][i]["actor"]["name"] is not None) and (obj["data"][i]["actor"]["username"] is not None) and (obj["data"][i]["transactions"][0]["target"]["name"] is not None) and (obj["data"][i]["transactions"][0]["target"]["username"] is not None) and (obj["data"][i]["message"] is not None)):
        x = 'ID: %s - %s (%s) sent $ to %s (%s) with message: [%s]'% (obj["data"][i]["payment_id"], obj["data"][i]["actor"]["name"], obj["data"][i]["actor"]["username"], obj["data"][i]["transactions"][0]["target"]["name"], obj["data"][i]["transactions"][0]["target"]["username"], obj["data"][i]["message"])
        print(x.translate(non_bmp_map))
        i+=1
