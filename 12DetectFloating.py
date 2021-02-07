# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lista1=[]
for i in range(int(raw_input())):
    
    n=bool(re.match(r"^[+-]?[0-9]*[.][0-9]+$",raw_input()))
    print(n)   
           
