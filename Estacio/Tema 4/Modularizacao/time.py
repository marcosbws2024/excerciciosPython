import time
print(time.time())
print(time.localtime())
x= time.time()
print(f'Local Time: {time.ctime(x)}')
