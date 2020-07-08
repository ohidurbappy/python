# --------comment--------------
#  First comment
name = 'Hashimpur'  # this is my village name
print(f"My village name is  {name}")
"""
Hello this is a documents 

"""

# --------multiple statement in single line
print("Hello")
print("World")

# ------- multiline statement -------------
number_of_fruits = 3 +\
    4 +\
    6

days=[
    "sunday","monday","thursday",
    "friday"
]

# -------- quotatioin -----------------
fruitName='Jackfruit'
flowerName="Lily"
fishName="""Hil
sha"""

# ---------waiting for the user ----------
# input("Press any key to continue...")

# ---------- suites -------------------
x=5
if x==5:
    print("x is equal to 5")
    print("It's 5")
    
# --------- assigning variable -----------
counter=100 # integer
length=50.4 # float
name="python" # string

print(counter)
print(length)
print(name)

a=b=c=1 # multiple assignment

a,b,c=1,45.7,"python"

# --------- data type -------------

var1=100 # number

del var1 # delete variable number

str1="Hello World"

print(str1)
print(str1[0])
print(str1[0:7])
print(str1[3:])
print(str1 + " Python")
print(str1 *3) 

# -------- list -------------
flist=["mango","jackfruit","banana","apple"]
mlist=[89,90,33,2]

print(flist)
print(mlist[0:4])
print(flist[0:])
totalList=flist[0:2]+mlist[0:2]
print(totalList)
print(flist*3)

# ---------- tuple ---------------
weekdays=('saturday','sunday','monday',
'tuesday','wednesday','thursday','friday')
mon=('jan','feb',1)
print(weekdays[0])
print(weekdays[3:75])
print(weekdays[4:])
print(weekdays[0:2]*2)
print(mon[1])

# ----------- dictionary ---------------
e2b={'a':'ekti','mango':'aam','mouse':'edur',3:"abid"}

print(e2b['a'])
print(e2b[3])
print(e2b.keys())
print(e2b.values())


# ----------- data type conversion -------------
age=20
print(age)
print(str(age))
length=50.5
print(int(length))
print(float(age))
complex_num=10+3j
print(complex_num)
x=1j*1j
print(x)
print(repr(weekdays))
print(eval("5*6"))


l=[3,66,2]
print(l)
print(tuple(l))
t=tuple(l)
print(t)
print(list(t))

f1=('one','mango')
f2=('two','bananna')
f3=('three','jack')
fruits=[f1,f2,f3]
d=dict(fruits)


print(d)

c=100
print(chr(c))

print(ord('a'))

print(hex(943))

print(oct(943))

print(bin(19))