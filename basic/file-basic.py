import os

# Open a file
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)
str = fo.read(10)
print ("Read String is : ", str)
print ("Closed or not : ", fo.closed)
fo.write( "Python is a great language.\nYeah its great!!\n")
print ("Opening mode : ", fo.mode)
fo.close()



# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)

# Close opened file
fo.close()


# create a file
f=open('hello.txt','w+')
f.close()
# rename a file
os.rename('hello.txt','world.txt')

# delete a file
os.remove('world.txt')

os.mkdir("myfiles/")

os.chdir('hello')