# while loop
count=9
while (count>=1):
    print(count)
    count-=1

# infinite loop
# while True:
#     print("Hello")


# loop with else statement
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


for i in range(2,5):
    print(i)

# making a list with range function
a=list(range(0,9))
print(a)

fruits=['mango','guava','jackfruit','banana','berry']

for f in fruits:
    print("I love ",f)

for i in range(len(fruits)):
    print(fruits[i])



for n in "Abidur":
    print(n)

num=[11,55,6,93,23,75,9]


for j in num:
    if j%2==0:
        print("List contains an even number")
        break

else:
    print("List does not contain an even number")              

for a in reversed(range(1,6)):
    for x in range(0,a):
        print("*",end="")
    print()

for b in range(1,21):
    for a in range(1,11):
        print(b*a,end=" ")
    print()


# ------ iteration ------------
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        print("Sorrryyyyyyyy!")
        exit()