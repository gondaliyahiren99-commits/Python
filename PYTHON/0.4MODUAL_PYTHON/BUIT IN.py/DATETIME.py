from datetime import datetime,timedelta
dt=datetime.now()#date and time both
print(dt)
print(dt.date())
print(dt.time())
print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.second)

#________________________
expiry=dt+timedelta(days=10)
print(expiry)
expiry_hour=dt+timedelta(microseconds=100000)
print(expiry_hour)