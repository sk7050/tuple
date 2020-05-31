
min=0
sec=0
ref=0
setting=1

while(setting==1):
    
    ref +=1

    
    if(ref==16500):
        
        sec=sec+1
      
        ref=0
    if(sec==60):

       min=min+1
       sec=0
       min=min%60
       if(min>=1):
           setting=int(input("continu=?, if yes press 1 or off prees 0 = "))
     
    
    print("\r",min,":",sec,":",ref,end="")  
      

