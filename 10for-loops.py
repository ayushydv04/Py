for i in range(143):
    print(i)


# iterating a list 
list=["cars","space","art","sports"]
for i in list:       #i kuch special nhi hai,aise hi ek word assign krr rakha hai
     print(i)


# iterating a tuple
tuple=(1,2,3,4,5,'jimmy')
for i in tuple:
    print(i)


# iterating a dict 
dict={
     "mahindra":"thar",
     "tata":"harrier",
     "ashok leyland":"taatra"
    }
for i in dict:   #ye sirf keys print krega
    print(i)

for i in dict.items():     #ye key aur values dono print krega
    print(i)

for key,value in dict.items():
    print(f"the company is {key} and car is {value}")


#print table of 2
for i in range(1,11):
    print("2 *",i,"=",2*i)


# (1,2,3) last waala gap decide krta hai
for i in range(1,21,3):
    print(i)



#FOR LOOP WITH ELSE
for i in range(5):
    print(i)
else:
    print("sorry")


for i in range(7):
    print(i)
    if i==5:
        break               #loop break nhi hua,khtm hua h ,islie else m nhi ghusega
    
else:
    print("sorry")





    