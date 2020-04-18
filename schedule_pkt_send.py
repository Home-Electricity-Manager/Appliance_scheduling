"""
@author : Jeevesh Juneja 
(https://github.com/Jeevesh8/)
"""

import utils
import device_feed_map as dfm
from data_sender import send
from threading import Timer

exp_pkt_send_delay = 500
scheduler_outfile = 'devices.csv'

time_to_devices_dic = utils.process_csv(scheduler_outfile)

device_feed_num_dic, elems_per_feed = utils.get_device_feed_num_dic( dfm.device_feed_dic )

feed_to_devices_dic = {}

for k, v in dfm.device_feed_dic.items() :
    if v not in feed_to_devices_dic :
        feed_to_devices_dic[v]=[]
    feed_to_devices_dic[v].append(k)

for timestamp, device_onoff_dic in time_to_devices_dic.items() :
    feed_dic = all_feeds_modified(device_onoff_dic)
    
    for feed, device_onoff_dic in feed_dic :
        onoff_lis = get_final_onoff_lis(feed, device_onoff_dic)

        t = Timer(timestamp-exp_pkt_send_delay, send, feed_no = feed,
                                                      onoff_lis = onoff_lis, time=timestamp, 
                                                      device_states = dfm.initial_device_states.copy())
        t.start()



def all_feeds_modified(device_onoff_dic) :
    #Returns a dictionary of all feeds modified, in format { feed : {device_modified: on/off,..}, ..}
    feed_dic = {}
    for device, onoff in device_onoff_dic.items() : 
        feed =  dfm.device_feed_dic[deivce]
        if feed not in feed_dic :
            feed_dic[feed] = {}
        feed_dic[feed][device] = onoff
    return feed_dic

def get_final_onoff_lis(feed, device_onoff_dic) :
    onoff_lis = []
    for device in feed_to_devices_dic[feed] :
        if device in device_onoff_dic :
            onoff_lis.append(device_onoff_dic[device])
            dfm.initial_device_states[device] = device_onoff_dic[device]
        else :
            onoff_lis.append(dfm.initial_device_states[device])
    return onoff lis