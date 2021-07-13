
import datetime
a = datetime.datetime.now()
print (a)

#
#
# <<<<<<<<<< code block >>>>>>>>>>
#

b = datetime.datetime.now()
print (b)

c = b - a

time = divmod(c.days * 86400 + c.seconds, 60)
print (time)

print(f'{time[0]} minutes',f'\n{time[1]} seconds')
