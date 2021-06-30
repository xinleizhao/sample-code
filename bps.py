from __future__ import division
from __future__ import print_function 
import sys 
import copy 
import pprint 
prev_value = {} 
prev_time = {} 
prev_bps = {} 

''' This function returns the delta of the counter between current and previous values ''' 
def interface_bytes_to_bps(index_name, direction, bytes_counter, **kwargs): 
    global prev_value
    global prev_time
    global prev_bps
    
    index_name_direction = index_name + "-" + direction
    cur_time = kwargs.get('point_time', 0) 
    bytes_counter = int(bytes_counter) 
    # convert bytes into bits 
    # bps = (bytes * 8) 
    bits_counter = bytes_counter * 8 
    cur_value = bits_counter 
    
    # calculate the time difference 
    time_difference = ( cur_time - prev_time.get(index_name_direction, 0) ) 
    
    if (time_difference == 0):
        print('__ERROR__ avoiding division by zero') # return zero to avoid division by zero 
        return 0 
    else: # Calculate data seen in bps 
        try: 
            bps = ( cur_value - prev_value.get(index_name_direction, 0) ) / time_difference
        except Exception: 
            print("error: exception caught!", file=sys.stderr) 
            bps = prev_value.get(index_name_direction, 0) 
            
        # update global variables 
        prev_value[index_name_direction] = cur_value 
        prev_time[index_name_direction] = cur_time 
        
        return bps
