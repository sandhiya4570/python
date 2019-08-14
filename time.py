from datetime import datetime
fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.strptime('2010-01-03 17:31:22', fmt)
daysDiff = (d2-d1).days
print daysDiff
> 2
minutesDiff = daysDiff * 24 * 60
print minutesDiff
> 2880
