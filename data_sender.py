from Adafruit_IO import Client, Feed, Data, RequestError
import device_feed_map as dfm 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--feed_no', help='Feed number to which to send data')
parser.add_argument('--onoff_lis', nargs = '*', help='0 for switching off, 1 for switching on; list of states of all devices on feed_no')
parser.add_argument('--time', help='UNIX timestamp for swithcing time')
args=parser.parse_args()

 
ADAFRUIT_IO_USERNAME = "Archit149"
ADAFRUIT_IO_KEY = "2619ba57dee340489754ca6dac5de74b"
 
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def send(feed_no=args.feed_no, onoff_lis=args.onoff_lis, time=args.time, device_states=dfm.initial_device_states) :
    try :
        feed = aio.feeds(feed_no)
    except RequestError :
        new_feed = Feed(name=feed_no)
        feed = aio.create_feed(new_feed)

    onoff_string = ''
    for elem in onoff_lis :
        onoff_string = onoff_string+','+str(elem)
    packet = args.time+','+ onoff_string
    aio.send_data(feed.key, packet)
    
    #if(success)
    dfm.write_files(initial_device_states=device_states)
