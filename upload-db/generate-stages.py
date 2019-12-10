import random
import time
from datetime import datetime, timedelta
import json

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def random_btw(start, end, prop):
    format = '%m-%d-%Y %H:%M'
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def random_forward(start, delta=1814400):
    random_second = random.randrange(delta)
    if random_second > 1209600 or start == None:
        return None
    else:
        return start + timedelta(seconds=random_second)

def random_cmpany():
    company = ['airbnb', 'amazon', 'apple', 'facebook', 'google', 'linkedin',
               'microsoft', 'netflix', 'salesforce', 'uber']
    n = random.randint(0, len(company) - 1)
    return company[n]

def convert_json(A):
    data = {
        'name': A[0],
        'applied': A[1],
        'phone': A[2],
        'onsite': A[3],
        'offer': A[4],
        'company': A[5]
    }
    return data

if __name__ == "__main__":
    with open('names.txt', 'r') as f:  # random names
        names = f.read().splitlines()

    filename = 'date_data.json'
    open(filename, "w").close()  # clean the output file

    for i in range(100):
        rand_st = random_btw("1-1-2020 00:00", "1-1-2021 00:00", random.random())  # generate random date between two dates
        line = [names[i], rand_st] # First and Second element

        st = datetime.strptime(rand_st, '%m-%d-%Y %H:%M')
        for _ in range(3):  # Third, Forth, Fifth element
            nxt_st = random_forward(st)
            if nxt_st == None:
                line.append(str(None))
            else:
                line.append(nxt_st.strftime("%m-%d-%Y %H:%M"))
            st = nxt_st

        line.append(random_cmpany())  # Sixth element
        date_data = convert_json(line)

        with open(filename, 'a') as json_file:
            json.dump(date_data, json_file)
            json_file.write("\n")

