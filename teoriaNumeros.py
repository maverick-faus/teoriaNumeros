import math

def dec2n(n,b):
    simbolos={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    q=n
    a = ''
    while q!=0:
       a=simbolos[q%b]+a
       q =q//b
    return a

def n2dec(n,b):
    simbolos={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15} 
    k=len(n)-1
    a=0
    for char in n:
        a= a+simbolos[char]*math.pow(b,k)
        k=k-1
    return a

def suma(a,b):
    a2=dec2n(a,2)
    b2=dec2n(b,2).zfill(len(a2))
    a2=a2.zfill(len(b2))
    n=len(a2)
    c=0
    s=''
    for j in reversed(range(0,n)):
        d=math.floor((int(a2[j])+int(b2[j])+c)/2)
        s = "{:.0f}".format(int(a2[j])+int(b2[j])+c-(2*d))+s
        c=d
    s="{:.0f}".format(c)+s
    return s

def multiply(a,b):
    a2=dec2n(a,2)
    b2=dec2n(b,2).zfill(len(a2))
    a2=a2.zfill(len(b2))
    n=len(a2)
    c=[]
    for j in reversed(range(0,n)):
        if int(b2[j]) ==1:
           c.append(a2.ljust(n+(n-1-j), '0'))
        else:
           c.append('0')
    p=0
    for elem in c:
        print(elem)
        p= n2dec(suma(p,n2dec(elem,2)),2)
    return p 

def division(a,d):
    q=0
    r= math.sqrt(a*a)
    d1=math.sqrt(d*d)
    while r>= d1:
        r=r-d1
        q=q+1
    if a<0 and r> 0 and d>0:
        r=d1-r
        q = -(q+1)
    if a>= 0 and d<0:
        r=d1-r
        q=q+1
    return(q,r)     

def exp(b,n,m):
    x=1
    k=len(n)
    power = b % m
    for i in reversed(range(0,k)):
        if int(n[i]) == 1:
            x = (x*power) % m
        power = (power*power) %m   
    return x

def gcd(a,b):
    x=min(a,b)
    y=max(a,b)
    while y != 0:
        r = x%y 
        x= y
        y =r
    return x
        
# Base 10 to base n -----------------------
n=input('Number in base 10: ') 
b=input('New base: ') 
basen=dec2n(n,b)
print(basen)
# Base n to base 10 -----------------------
#base10 = n2dec(basen,b)
base10 = n2dec((str)(input('Number in base n: ')) ,input('Base: ') )
print(base10)
# Binary Sum -----------------------
s =suma(input('First numbrer to sum: '),input('Second number to sum: '))
print(s, n2dec(s,2))
# Binary Product -----------------------
m = multiply (input('First numbrer to multiply: '),input('Second number to multiply: '))
#m = multiply (985,486)
print(m)
# Division algorithm -----------------------
d=division(input('Dividend: '),input('Divisor: '))
print(d)
# Modular exponentiation -----------------------
print(exp(input('Base:'),dec2n(input('Exponent:'),2),input('Modulo:')))
# Euclidean algorithm -----------------------
print(gcd(input('a:'),input('b:')))