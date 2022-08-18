from datetime import date, timedelta, datetime
today = date.today()

#  1st solution of yesterday
yesterday = today - timedelta(days=1)
print("today's date:", today)
print("yesterday's date:", yesterday)

# 2nd solution of market close time problem
pre_market_time = '9:15'


def market_close_time(t1, t2):
    split_t1 = t1.split(":")
    split_t2 = t2.split(".")

    if len(split_t2) == 1:
        a = 0
        b = 0
    else:
        a = int(split_t2[1])
        b = int(split_t1[1])

    h = 60
    m = a+b
    hr = (h*int(split_t1[0]))+h*int(split_t2[0])
    hr = int(hr/h)
    flag = True
    while (flag == True):
        if hr > 12:
            hr = hr-12
        if hr <= 12:
            break
    if m > h:
        m = m-60
        return (f"Market close time: {hr+1}:{m}")
    else:
        return (f"Market close time: {hr}:{m}")


var = market_close_time(pre_market_time, '2.22')
print(var)

# 3rd difference between threading and multiprocessing


''' The thread is created by a process. Every time you open an application, it itself creates a thread which will handle all the tasks of that specific application. Like-wise the more application you open more threads will be created.The threads are always created by the operating system for performing a task of a specific application. basically thread is virtual components or codes, which divides the physical core of a CPU into virtual multiple cores, in the other side  Multiprocessing is the ability for computers to complete multiple tasks at the same time without having to wait for one task to complete before the next task can be started. A dual-core processor is twice as fast as a single processor
like you use music player and visual studio code at same time '''
