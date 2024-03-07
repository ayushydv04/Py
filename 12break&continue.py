for i in  range(11 ):
    print("2 *",i,"=",i*2)
    if (i==8):
        break       #loop ko chhod ke nikal jaao, iske baad ki saari value htaa do



for i in  range(11 ):
    if (i==5):
       continue     # itetration ko chhod ke nikal jaao , sirf iss particular value ko htaa do
    print("2 *",i,"=",i*2)


#EMULATING DO-WHILE LOOP
i=0      
while True:
    print (i)
    i=i+1
    if (i%10==0):  #jab i divide by 10 = 0 tab function break ho jaayega
        break
