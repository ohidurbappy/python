import time

ticks=time.time()

print("No of seconds elapsed:",ticks)

print(time.localtime())

print("Localtime:",time.localtime(time.time()))

ftime=time.asctime(time.localtime(time.time()))

print("Time:",ftime)

# calendar for a month

import calendar

cal=calendar.month(2020,4)

print("Calendar".center(50,"*"))
print(cal)

print(calendar.calendar(2020,w=2,l=1,c=6))


print("time.altzone",time.altzone)

# find time taken by a process

def myprocess():
    time.sleep(2.5)




t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d = time.mktime(t)
print ("time.mktime(t) : %f" %  d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))

print("First day of week:",calendar.firstweekday())

print("Is 2020 leap year:",calendar.isleap(2020))

print("No of leap days within 2000 and 2040:",calendar.leapdays(2000,2040))
