# Russion peasant multiplication technique
# Ref: https://www.udemy.com/python-the-next-level/learn/#/lecture/224870

def russian(a,b):
    x=a;y=b
    z=0
    while x>0:
        if x%2==1:z=z+y
        x=x >>1
        y=y <<1
    return z

print (russian(16,24))
