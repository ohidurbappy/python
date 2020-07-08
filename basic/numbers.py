import math
import random
a = 8
del a
try:
    print(a)
except NameError:
    print("Error!")

hex_num = 0x999
print(hex_num)
print(int(6e12))

# mathematical functions
print(abs(-76.9))
print(math.ceil(33))
print(math.exp(6.9))
print(math.fabs(-76))
print(math.floor(33.44))
print(math.log(10))
print(math.log(math.exp(10)))
print(math.log10(10))
print(min(1,9,33,-99,1.9))
print(max(1,9,33,-99,1.9))
print(math.modf(-56.8))
print(pow(2,3))
print(round(79.467,2))
print(math.sqrt(25))

# random number functions
print(random.choice(['a','b','c','d']))
print(random.randrange(0,20,2))
random.seed()
print(random.random())
flist=['a','c','h','o']
random.shuffle(flist)
print(flist)
print(random.uniform(2,5))

# mathematical constants
print(math.pi)
print(math.e)


# trigonometric function

print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(90)))

x=4
y=5
print(math.hypot(x,y))

print(math.radians(360))
print(math.degrees(1.57))
