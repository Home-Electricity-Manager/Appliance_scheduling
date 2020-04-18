from Adafruit_IO import Client, Feed, Data, RequestError
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--feed_no', help='Feed number to which to send data')
parser.add_argument('--elems_in_feed', type=int, help='Total number of devices connected to the feed')
parser.add_argument('--device_no', type=int, help='Device whose state has to be changed')
parser.add_argument('--onoff', type=bool, help='0 for switching off, 1 for switching on')
parser.add_argument('--time', help='UNIX timestamp for swithcing time')
args=parser.parse_args()


ADAFRUIT_IO_USERNAME = "Archit149"
ADAFRUIT_IO_KEY = "2619ba57dee340489754ca6dac5de74b"
 
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try :
    feed = aio.feeds(args.feed_no)
except RequestError :
    new_feed = Feed(name=args.feed_no)
    feed = aio.create_feed(new_feed)

onoff_string = ''
packet = args.time+','+ onoff_string

