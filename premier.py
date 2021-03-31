r=1
while r==1 : 
    n=int(input('entrer un nombre : '))
    for k in range(2,n,1):
        if n%k!=0 :
          print("ce nombre  est  premier")
          break
        elif n%k==0 :
          print("ce nombre n est  premier")
          break
            
    r=int(input("0/1:"))
         
    
    
