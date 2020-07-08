
file=open("quotes.txt")

print(file.readline())

print(file.read())


file.close()


with open("quotes.txt") as file:
    print(file.readline())