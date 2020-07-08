a=3
if (a==3):
    print("a is 3")

print("Hi, there! What's your name?\n")
name=input()
print("What's your mark, " + name + "?")
mark=int(input())
if (mark >= 33):
    print("Congratulations! You've passed.")
elif(mark < 33 & mark < 0):
    print("You've failed.")
else:
    print("Really?")
