# TYPES OF COLLECTION
# list
# tuple
# dictionary
# set
                        #  LISTS []

states=["bihar","punjab","kerala","haryana"]   #list 
states[2]="tamil nadu"      #lists are mutable, values can be changed
print(states)
print(len(states))

states.append("gujarat")    #append add the ittem at the end of list
print(states)

states.sort()

states.insert(1,"mp")  #insert add item at the desired position
print(states)

states.remove("gujarat")    #remove removes an element
print(states)

states.pop()                #pop removes the last element
print(states)               #can specify the index in brackets also

# del states
# print(states)



                     #TUPLES ()

mycars=("camaro","hellcat","r35 nizmo")   #tuples are immutable, values cannot be changed9
print(type(mycars))
# mycars[2]="challenger"
# print(mycars)  error-'tuple' object does not support item assignment
# change krr skte h agar datatype change krr de to  
# ek value ka tuple nahi hota,agar chahie to vo value ke baad comma lagana padega
temp=list(mycars)
temp.append("mustang")
temp[1]="challenger hellcat"
Cars=tuple(temp)
print(Cars)

tup=(1,3,5,4,3,2,7,55,2,4,56,7)
res= tup.count(3)        #3 kitni baaar print hua hai
res= tup.index(3)        #3 ppehli baar konse index pe aaya hai 
print(res)






                    #DICTIONARY {}

d={"name":"jimmy",       #key and value pairs 
   "roll.no":"02",
   "registration":"12314293"
   } 
print(d)  
print(d["roll.no"])  
print(d.keys())          #keys print all the keys of dict.
print(d.values())        #values print all the values of dict
print(d.pop("roll.no"))
print(d.popitem())      #last value remove krr deta h
d["college"]="lpu"       #to insert in a dictionary
print(d)





                    #SETS {}

set={1,2,3,4,57,6,54,3,3}
print(set)             #set does not print repeated values

set.add(34)            #add only 1 element
print(set)            
 
set.update([99,43,2])  #update can add multiple elements
print(set)
 
























