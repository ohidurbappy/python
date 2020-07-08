import math

def getRoot(number):
    "This function finds the root of a number"
    return math.sqrt(number)


print("The square root of 100 is:",getRoot(100))


def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)



# Function definition is here
def printinfo( name, age=22 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 50, name = "ohidur" )
printinfo(name="Bappy")



def printBooks(*books):
    return ", ".join([book for book in books])



print("I have ",printBooks("C","C++","Python")," books")



# lambda function

sum=lambda num1,num2: num1+num2

print("Sum of 10 and 12 is:",sum(10,12))


