def count():
    fopen = open("access.log","r")
    firefox = []
    chrome = []
    other = []
    for line in fin:
        if "Firefox/" in line:
            firefox.append(line)
        elif "Chrome/" in line:
            chrome.append(line)
        else: 
            other.append(line)
    print("No of request per browser are as follows:")
    print("Firefox",len(firefox))
    print("Chrome",len(chrome))
    print("Other",len(other))

count()
