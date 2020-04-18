import os
import pickle
import fileinput


def write_files(device_feed_dic=None, initial_device_states=None) :
    if device_feed_dic is not None :
        with open('device_feed_dic.pkl', 'wb+') as f :
            pickle.dump(device_feed_dic, f)
    if initial_device_states is not None :
        with open('initial_device_states.pkl', 'wb+') as f :
            pickle.dump(initial_device_states, f)    

def read_files() :
    with open('device_feed_dic.pkl', 'rb') as f :
        device_feed_dic = pickle.load(f)
    with open('initial_device_states.pkl', 'rb') as f :
        initial_device_states = pickle.load(f)
    return device_feed_dic, initial_device_states        

try :
    device_feed_dic, initial_device_states = read_files()    
except FileNotFoundError :
    device_feed_dic, initial_device_states = make_new_dic()


def update_device_feed_dic(device_name, new_feed_number) :
    ''' When shifting device from one switch-board to another'''
    assert(new_feed_number<=int(os.environ.get('N_FEEDS')))
    device_feed_dic[device_name] = new_feed_number


def add_new_device(new_device_name, new_feed_number, write=1) :
    assert(new_device_name not in device_feed_dic)
    device_feed_dic[new_device_name] = new_feed_number
    initial_device_states[new_device_name] = 0
    if write :
        write_files(device_feed_dic, initial_device_states)
        
def make_new_dic(files=None) :
    '''
    Input any file/stdin having "<device_name>:<feed_num>" in each line.(No space on either side of ':')
    <feed_num> must be element of [0,N_FEEDS-1]
    Makes new dictionary of format {'device_name' : feed_number}
    feed_number is string in final dictionary.
    '''    
    device_feed_dic = {}
    initial_device_states = {}
    
    for line in fileinput.input(files=files) :
        line = line.rstrip()
        new_device_name, new_feed_number = line.split(':')
        add_new_device(new_device_name, new_feed_number, write=0)
        initial_device_states[new_device_name] = 0
    
    write_files(device_feed_dic, initial_device_states)
    return device_feed_dic, initial_device_states