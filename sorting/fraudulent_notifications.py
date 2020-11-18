import bisect

def activityNotifications(expenditure, d):
    counter = 0
    trailling_days = sorted(expenditure[:d])
    pointer1 = d//2
    pointer2 = pointer1-1

    is_odd = d%2

    for position, transaction in enumerate(expenditure[d:]):
        if is_odd:
            median = trailling_days[pointer1] 
            if transaction >= 2*median:
                counter += 1
        else:
            median = trailling_days[pointer1]+trailling_days[pointer2]
            if transaction >= median:
                counter += 1

        del(trailling_days[bisect.bisect_left(trailling_days, expenditure[position])])
        bisect.insort_left(trailling_days, transaction)
    
    return counter
