import datetime
print(datetime.datetime.now)

current_time=datetime.datetime.now()
print(f"date :{current_time.date()}")
print(f"date only:{current_time.date()}")
print(f"month :{current_time.month}")
print(f"year :{current_time.year}")