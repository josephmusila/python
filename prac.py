def musila():
    print("im here")
  
musila()
def add(*num):
    print(sum(num))

add(7,9,9,0,7)



def names(fname,lname="lop"):
     print("hi"  +fname+lname+  "yoa are wecome")    

names("john")      
def user(**like):
 print(like)
user(like1="lan",like2="lex") 

def add(a,b):
    return a+b
add(1,3)
sum=add(5,10)
print(sum)

pi=3.14
def area(radius):
 return pi*(radius**2)
def volume(radius):
    return 4/3*pi*(radius**3)
