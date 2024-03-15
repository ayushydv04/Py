a=input("Enter the number:")
a=input("Enter the number:")                                            
print(f"Multiplication table of {a} is ")
try:                                        #try krke dekho ye code,agar work krta h to theek nhi to except print karega
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Datatype Error")
finally:
    print("End")                    # finally ke andar ka code hamesha run krta h whether code mai error ho ya no ho 
                                    # finally function jab define hota h tab b hi use hota h, return case m bhi print hoga finally 

try:
    a=int(input("Enter the number1:"))
    b=int(input("Enter the number2:"))
    print (a/b)
except ArithmeticError:
    print("Error")   
finally:
    print("end of program") 

a=[1,2,3]
try:
    print("Second element = %d"%(a[1]))
    print("Fouth  element = %d"%(a[3]))
except IndexError:
    print("an eror occured")


