import arrow
import time
import os

os.environ['TZ'] = 'America/New_York'
time.tzset()
print(time.strftime('%X %x %Z'))
print(arrow.now())