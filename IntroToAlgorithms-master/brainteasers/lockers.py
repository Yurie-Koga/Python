
import random

    # 100 Lockers
def lockers():
    lockers = []  # 1 means open, 0 means close
    # day one
    for i in range(100):
        lockers.append(1)

    # from day two to day 100 (99 days)
    for day in range(2, 100):
        for l in range(100):  # for all lockers
            if l % day == 0:  # every day'th locker
                # toggle
                if lockers[l] == 1:
                    lockers[l] = 0
                else:
                    lockers[l] = 1

    count = 0
    for n in range(len(lockers)):
        if lockers[n] == 1:
            count += 1
    print(count)