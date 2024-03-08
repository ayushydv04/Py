#FOUR types of arguments - default,variable length,required,keyword

#REQUIRED

def calculategmean(a,b):   # calculategmean function ka naam hai aur a and b function ke arguments
    mean=(a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if (a>b):        
        print("First number is greater")
    else:
        print("Second number is greater")

def islesser(a,b):
    pass                           #if function ki body define nahi krni h abhi to, pass use krr skte h
# a=10
# b=20
# gmean1=(a*b)/(a+b)
# print(gmean1)

# c=2
# d=5
# gmean2=(c*d)/(c+d)
# print(gmean2)

#INSTEAD OF DOING THIS WE WILL USE THE FUNCTION

a=10
b=2
calculategmean(a,b)
isgreater(a,b)

c=2
d=5
calculategmean(c,d)
isgreater(c,d)


def average(a,b):
    avg=(a+b)/2           # OR print((a+b/2))
    print(avg)
a=4
b=8
average(a,b)


def average(*numbers):  #* - tuple datatype ke liye hai, ** - dictionary ke liye
    sum=0
    for i in numbers:
        sum=sum+i
        #print(sum/len(numbers))
    return sum/len(numbers)         #return ke liye ek storing variable lagega,fir vo variable print krna hai
c=average(1,2,3,4)
print(c)