import os
import datetime
import pickle
from device_feed_map import device_feed_dic

def get_device_feed_num_dic(device_feed_dic) :
    '''
    Returns a dictionary , {device : its number in its feed(string)}
    and a list : lis[i] = devices on (i+1)th feed (Total N_FEEDS feeds are there) 
    '''
    dic = {}
    lis = [0 for i in range(int(os.environ.get('N_FEEDS')))]
    i=0
    for k , v in device_feed_dic.items() :
        dic[k] = str(lis[int(v)])
        lis[int(v)]+=1
    return dic, lis

def process_csv(file) :
    '''
    Processes csv file of format:-  device_name, time, on/off 
    Makes a txt file which will contain commands(for sending data) to execute 
    '''
    device_feed_num_dic, elems_per_feed = get_device_feed_num_dic(device_feed_dic)
    
