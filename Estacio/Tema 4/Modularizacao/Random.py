import random

for i in range(10):
    vnr = random.random()
    vnr1 = random.getstate()
    
    print(vnr)
    print(vnr1)