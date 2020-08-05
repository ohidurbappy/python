import os
import datetime

file = open("quotes.txt")
print(file.readline())
print(file.read())
file.close()

with open("quotes.txt") as file:
    print(file.readline())

with open("quotes.txt") as file:
    for line in file:
        print(line.upper())

f = open("quotes.txt")
lines = f.readlines()
f.close()
lines.sort()
print(lines)


# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")
# else:
#     with open("hello.txt",'w') as f:
#         f.write("hello")

# if os.path.exists("hello.txt"):
#     try:
#         os.rename("hello.txt","world.txt")
#     except FileExistsError:
#         print("File Already exists!")


file_size=os.path.getsize('hello.txt')

print("File Size: {}".format(file_size))

file_date_modified=os.path.getmtime("hello.txt")
file_date_created=os.path.getctime("hello.txt")


file_date_created=datetime.datetime.fromtimestamp(file_date_created)
file_date_modified=datetime.datetime.fromtimestamp(file_date_modified)


print("File Date Created: ",file_date_created)
print("File Date Modified: ",file_date_modified)

print("Is it file: ",os.path.isfile("hello.txt"))

file_absolute_path=os.path.abspath("hello.txt")

print("Absolute path: ",file_absolute_path)


# working with dir

current_dir=os.getcwd()

print("Current Working dir: ",current_dir)

if not os.path.exists("new_dir"):
    os.mkdir("new_dir")

os.chdir("new_dir")

os.chdir("../../")

current_dir=os.getcwd()

for item in os.listdir(current_dir):
    fullname=os.path.join(current_dir,item)

    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is not a directory".format(fullname))

