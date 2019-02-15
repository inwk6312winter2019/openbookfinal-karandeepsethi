import operator

def topipaddress():
    d = dict()
    fopen = open("access.log","r")
    for line in fopen:
        if "GET /" in line or "POST /" in line:
            ip = line.split('-')[0]
            if ip not in d:
                d[ip] = 1
            else:
                d[ip] += 1
    new = sorted(d, key=d.get, reverse=True)[:20]
    return new


print(topipaddress())
