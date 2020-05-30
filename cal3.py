temp=0
count=0
ex="y"
Op="+"
while(ex=="y"):
    N=int(input("input Number="))
    if(Op=="+"):
        temp=temp+N
    elif(Op=="-"):
        temp=temp-N 
    elif(Op=="*"):
        temp=temp*N 
    elif(Op=="/"):
        temp=temp/N 
    count+=1  
    if(count<2):
        ex="y" 
    else:

        ex=input("Do you want to Continue(if yes type y and if No type n)??=")
    if (ex=="y"):
        Op=input("what do you want(EX:+ , - ,* ,/ )= ")
        
         
    
   
print("total Calculation="+str(temp))                
