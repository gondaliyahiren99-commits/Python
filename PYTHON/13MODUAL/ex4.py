
from datetime import datetime ,timedelta

current_time=datetime.now()
print(current_time.time())
print(current_time.hour)
print(current_time.minute)

print(current_time)
expiry=current_time+timedelta(hours=10)
print(expiry)