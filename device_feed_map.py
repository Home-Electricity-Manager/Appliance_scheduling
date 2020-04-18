import os
import pickle
import fileinput

try :
    with open('device_feed_dic.pkl', 'rb') as f :
        device_feed_dic = pickle.load(f)
except FileNotFoundError :
    make_new_dic()


def update_device_feed_dic(device_name, new_feed_number) :
    ''' When shifting device from one switch-board to another'''
    assert(new_feed_number<=int(os.environ.get('N_FEEDS')))
    device_feed_dic[device_name] = new_feed_number


def add_new_device(new_device_name, new_feed_number, write=1) :
    assert(new_device_name not in device_feed_dic)
    device_feed_dic[new_device_name] = new_feed_number
    if write :
        with open('device_feed_dic.pkl', 'wb+') as f :
            pickle.dump(device_feed_dic, f)
        
def make_new_dic(files=None) :
    '''
    Input any file/stdin having "<device_name>:<feed_num>" in each line.(No space on either side of ':')
    <feed_num> must be element of [0,N_FEEDS-1]
    Makes new dictionary of format {'device_name' : feed_number}
    feed_number is string in final dictionary.
    '''    
    device_feed_dic = {}
    for line in fileinput.input(files=files) :
        line = line.rstrip()
        new_device_name, new_feed_number = line.split(':')
        add_new_device(new_device_name, new_feed_number, write=0)
    with open('device_feed_dic.pkl', 'wb+') as f :
        pickle.dump(device_feed_dic, f)    
