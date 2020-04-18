import os
import datetime as dt
import pickle
import csv
from device_feed_map import device_feed_dic, initial_device_states

def get_device_feed_num_dic(device_feed_dic) :
    '''
    Returns a dictionary , {device : its number in its feed(string)}
    and a list : lis[i] = no. of devices on (i+1)th feed (Total N_FEEDS feeds are there) 
    '''
    dic = {}
    lis = [0 for i in range(int(os.environ.get('N_FEEDS')))]
    i=0
    for k , v in device_feed_dic.items() :
        dic[k] = str(lis[int(v)])
        lis[int(v)]+=1
    return dic, lis

def get_time_stamp(now, simple_time) :
    '''
    simple_time == nearest hour:minute to occur in future
    returns seconds passed from january 1, 1970 to simple_time
    Caution :- Never run this just few miliseconds before data is to be sent; it might be assumed to be of next day
    '''
    hour, minute = simple_time.split(':')
    hour, minute = int(hour), int(minute)
    scheduled_time = now.replace(hour=hour, minute=minute)
    if scheduled_time<now :
        scheduled_time = scheduled_time.replace(day=scheduled_time.day+1)
    return scheduled_time.timestamp()

def process_csv(file_name='devices.csv') :
    '''
    Processes csv file of format:-  device_name, time, on/off 
    time == hour : minute           hour is element of [0,23]. minute is element of [0,59]
    Returns dictionary of format { timestamp : { device_to_change:on/off, .. }, ..}
    '''
    device_change_time = {}
    
    with open(file_name) as f :
        csv_reader = csv.reader(f, delimiter=' ')
        now = dt.datetime.today()
        for row in csv_reader :
            timestamp = get_time_stamp(now, row[1])
            
            if timestamp not in device_change_time :
                device_change_time[timestamp] = {}
            
            device_change_time[timestamp][row[0]] = row[2]
    
    return device_change_time    

    