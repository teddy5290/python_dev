import datetime

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

batch_dt='202201'
# batch_y=batch_dt[:4]
# batch_m=batch_dt[4:]


# print (batch_y)
# print (batch_m)
batch_end_dt=last_day_of_month(datetime.date(int(batch_dt[:4]), int(batch_dt[4:]), 1))
print(batch_end_dt )
batch_end_dt_yb=batch_end_dt.strftime("%b-%y")   ## ex.Feb-22
print (batch_end_dt_yb )
