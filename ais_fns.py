import time
from datetime import datetime
import pytz

def get_event_timestamp(**kwargs):
    #print ("[mdavala] {}".format(kwargs))
    point_time = kwargs['point_time']
    #local_time = datetime.now(timezone('Hongkong'))
    #tz = pytz.timezone('Hongkong')
    #tz = pytz.timezone('Asia/Bangkok')
    tz = pytz.timezone('Asia/Taipei')
    dt = datetime.fromtimestamp(point_time, tz)
    event_time = dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    #print ("[mdavala] {}".format(event_time))
    return event_time
