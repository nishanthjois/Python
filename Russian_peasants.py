# Russion peasant multiplication technique with cache (saves almost 50% of time)

import time

CACHE = {}

def russian(a,b):
    key = (a,b)
    if key in CACHE:
        z= CACHE[key] ## Cache - do not run algo if key is already computed
    else: 
        x=a;y=b
        z=0
        while x>0:
            if x%2==1:z=z+y
            x=x >>1
            y=y <<1
        CACHE[key]=z ## Store the result in cache
    return z

startTime = time.time()
print (russian(16,24))
print ("Before %f" % (time.time()-startTime))

startTime = time.time()
print (russian(16,24))
print ("After %f" % (time.time()-startTime))



