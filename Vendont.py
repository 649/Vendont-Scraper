#!/usr/bin/env python """
from urllib.request import urlopen
import time
import json
import datetime

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
                          Version: 1.0

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

limit = input('Enter the maximum amount transactions to collect: ')
print('')
vjson = urlopen("https://venmo.com/api/v5/public?since=%s&until=%s&limit=%s" %(epoch, epoch2, limit))
obj = json.load(vjson)
#print(obj["data"])
limit = int(limit)
for i in range(0, limit):
    print('ID: %s - %s (%s) sent $ to %s (%s) with message: [%s]'% (obj["data"][i]["payment_id"], obj["data"][i]["actor"]["name"], obj["data"][i]["actor"]["username"], obj["data"][i]["transactions"][0]["target"]["name"], obj["data"][i]["transactions"][0]["target"]["username"], obj["data"][i]["message"]))