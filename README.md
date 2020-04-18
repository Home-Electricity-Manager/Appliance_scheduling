# Appliance_scheduling

## To start sending packets after producing scheduling output

``` python schedule_pkt_send.py```

Keep the computer on after this. 

The packets are of format timestamp,0/1,0/1,0/1.. where 0,1 denotes whether the device should be on or off.

There is a digit corresponding to each device connected to a feed.

When the program is run for the first time, it expects input from stdin , in the format device_name:feed_no, each entry in a new line. To stop adding new values, enter 000 . You can also provide a file, for taking these entries from in make_new_dic function in device_feed_map.py.
