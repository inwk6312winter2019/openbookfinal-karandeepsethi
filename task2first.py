def write_log():
    fin = open("access.log","r")
    fget = open("get.log","w")
    fpost = open("post.log","w")
    fput = open("put.log","w")
    fdelete = open("delete.log","w")
    for line in fin:
        if "GET /" in fin:
            fget.write(line)
        elif "POST /" in fin:
            fpost.write(line)
        elif "PUT /" in fin:
            fput.write(line)
        else:
            fdelete.write(line)


print(write_log())
