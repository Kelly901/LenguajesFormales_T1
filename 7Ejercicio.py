def is_leap(year):
    leap = False
    if year==1800 or year==1900 or year==2100 or year==2200 or year==2300 or year==2500:
        return False
    elif (year%4)==0 or year%400==0:
        return True
    
     
    
    return leap
year = int(raw_input())