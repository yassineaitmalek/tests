n=int(input('entrer le nombre du copies : '))
if n<10 :
    s=n*0.5
elif 10<n<20 :
    s=n*0.35
else :
    s=n*0.5
print('le prix à payer est : ',s,' DH ')