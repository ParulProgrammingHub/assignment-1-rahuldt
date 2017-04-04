a=[]
c=0
for i in range (0,5):
    b=input("enter the mark out of 100= ")
    a.append(b)
    c+=b
d=c/5
print "mean of marks is ",d
print "percentage of mark is ",d,"%"
if d<35:
    print "your fail"
else:
    print "your pass"
