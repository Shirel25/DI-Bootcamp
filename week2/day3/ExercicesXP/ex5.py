from datetime import datetime 

now = datetime.now() # current date and time
print("Current time : ", now)

if now.month == 1 and now.day == 1:
    next_year = now.year # It's already january 1st
else:
    next_year = now.year + 1

january_first = datetime(next_year, 1, 1, 0, 0, 0) 

time_left = january_first - now

hours, sec_remainder = divmod(time_left.seconds, 3600) # hours = time_left.seconds // 3600
                                                   # sec_remainder = time_left.seconds % 3600
minutes, seconds = divmod(sec_remainder, 60)

print(f"The 1st of January is in {time_left.days} days and {hours:02}:{minutes:02}:{seconds:02} hours") # 2 digits for each : 02
