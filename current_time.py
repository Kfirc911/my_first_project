import time
from datetime import datetime


now = datetime.now()

CURRENT_TIME = now.strftime("%H:%M:%S")
list_time = CURRENT_TIME.split(":")
for hour in range(int(list_time[0]),24):
    for min in range(int(list_time[1]),60):
        for sec in range(int(list_time[2]),60):
            print(hour," ",min," ",sec)
            time.sleep(1)