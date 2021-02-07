from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
lista=[]

for i in range(n):
    i=i+1
    lista.append(i)
    
c=""
for b in lista:
    c=str(c)+str(b)
   
    
print(c)