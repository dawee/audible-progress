from datetime import timedelta
import sys
from time import strptime


progress, total = (timedelta(hours=tm.tm_hour, minutes=tm.tm_min, seconds=tm.tm_sec)
                   for tm in (strptime(arg, '%H:%M:%S') for arg in sys.argv[1:3]))

print(f'{round(progress.total_seconds() * 100 / total.total_seconds())}%')
