#------ arithmetic operators -----------
a=13
b=9
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(b**2)
print(a//b)

#------- comparison operator ----------
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

# ------------assignment operator ----------

c=a+b
print(c)
c+=a
print(c)
c-=a
print(c)
c*=a
print(c)
c/=a
print(c)
c%=a
print(c)
c//=a
print(c)
c**=a
print(c)

#------- bitwise operators -----------
a=5
b=3
print(bin(a))
print(bin(b))
print(bin(a&b))
print(a|b)
print(a^b)
print(~a)
d=345
d<<=5
print(d)

#------- logical operators -------
a=True
b=False
x=True
y=False
print(a and b)
print(a and x)
print(b and y)
print(a or b)
print(a or x)
print(b or y)
print(not(a and b))

#---------- membership operators --------
mon=['jan','feb','mar']
print('jan' in mon)
print('feb' not in mon)
print('a' not in mon)

#----------- identity operators ----------
x=5
if x is 5:
    print("x is equal to 5")
if x is not 9:
    print("x isn't equal to 9")