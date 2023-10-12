import datetime as dt

time_millis = 10000000000

def millis_to_hhmmss(start_ms):
    hhmmss = dt.timedelta(milliseconds=start_ms)
    print(hhmmss)
    return str(hhmmss).split(".")[0]

new_time = millis_to_hhmmss(time_millis)
print(new_time)