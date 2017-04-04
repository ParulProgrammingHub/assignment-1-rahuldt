def ci(a,b,c):
    d=a*(1+c/12)**(12*b)
    print "compound intrest is ",d
a=input("enter principal amount= ")
b=input("enter timein year= ")
c=input("enter rate= ")
ci(a,b,c)
