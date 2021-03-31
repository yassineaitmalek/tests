def day_of_the_week(y,  m, d) : 
  
    # array with leading number of days values 
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
           
    # if month is less than 3 reduce year by 1 
    if (m < 3) : 
        y = y - 1
           
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
      
      
# Driver Code 

day = int(input("entrer the day : "))
month = int(input("entrer the month : "))
year = int(input("entrer the year : "))

if day_of_the_week(year, month, day)==0:
    print("the day is sunday")
elif day_of_the_week(year, month, day)==1:
    print("the day is monday")
elif day_of_the_week(year, month, day)==2:
    print("the day is tuesday")
elif day_of_the_week(year, month, day)==3:
    print("the day is wednesday")
elif day_of_the_week(year, month, day)==4:
    print("the day is thursday")
elif day_of_the_week(year, month, day)==5:
    print("the day is friday")
elif day_of_the_week(year, month, day)==6:
    print("the day is saturday")
 