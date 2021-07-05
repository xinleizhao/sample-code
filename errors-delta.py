from __future__ import division
from __future__ import print_function
import sys
import copy
import pprint

prev_value = {}
prev_time = {}
prev_errors = {}

'''
This function returns the delta of the counter between current and previous values
'''
def errors_delta(index_name, direction, errors_counter, **kwargs):
    global prev_value
    global prev_time
    global prev_errors

    index_name_direction = index_name + "-" + direction

    cur_time = kwargs.get('point_time', 0)
    errors_counter = int(errors_counter)

    cur_value = errors_counter

    # calculate the time difference
    time_difference = ( cur_time - prev_time.get(index_name_direction, 0) )

    if (time_difference == 0):
        print('__ERROR__ avoiding division by zero')

        # return zero to avoid division by zero
        return 0
    else:
        # Calculate error delta
        try:
            error_delta = ( cur_value - prev_value.get(index_name_direction, 0) ) / time_difference
        except Exception:
            print("error: exception caught!", file=sys.stderr)
            error_delta = prev_value.get(index_name_direction, 0)

        # update global variables
        prev_value[index_name_direction] = cur_value
        prev_time[index_name_direction] = cur_time

        return error_delta
