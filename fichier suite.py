n=int(input('entrer un rang :'))
k=0
s=2
b=0
fi=open('serie.txt','w')
fi2=open('resultat.txt','w')
while k<n :
    s=5*s+4
    b+=s
    k+=1
    fi.write('\n'+str(s))
    fi2.write('\n'+str(b))
    
fi.close()
fi2.close()