var1="Hello World"

print(var1[3:])

print(var1[:6]+"Python")

print("hello " * 5)
print("H" in var1)
print("H" not in var1)

print(r"Hello\nWorld")

m="mango"
print("My name is %s and I love %s"%('Bappy',m))

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

name="ohidur"

print(name.capitalize())

print(name.center(30,"*"))

str1 = "this is string example....wow!!!"
print (str1.ljust(50, '*'))

print (str1.rjust(50, '*'))



big_str='''Hello I am ohidur, I am from Bangladesh.
I am writing this program to learn basic python. python is 
an interesting language.'''

print("No of time python: "+ str(big_str.count('python')))

bangla_str='আমার সোনার বাংলা'
encoded=bangla_str.encode('UTF-8')
print(encoded)

print(encoded.decode('UTF-8'))

t='ohidur rahman'

print(t.endswith('rahman'))

t='Hello\t world\t python'

print(t.expandtabs(tabsize=20))

t="Hello world"

print(t.find('llo'))

print(t.find('War'))


t='ohid43'

print(t.isalnum())

print(t.isalpha())

print(t.isascii())

print("019293".isdigit())

print("01020".isnumeric())

print("    ".isspace())

print("Hello World".istitle())

print("Hello".join(["World","python"]))

print(len("Hello"))

print("Hello".upper())

print("HeLLo".lower())

print("  hey ".lstrip())

# make trans
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str1 = "this is string example....wow!!!"
print (str1.translate(trantab))

# max min
str1 = "this is a string example....really!!!"
print ("Max character: " + max(str1))

str1 = "TUTORIALSPOINT"
print ("Min character: " + min(str1))


str1="   Hey buddy      "
print(str1.strip())

print('H e l l o'.split(' '))

lst='''Hello
World
Python'''

print(lst.splitlines())

print("Hello World".startswith('Hell'))

print("thE hAUntEd hOUsE".swapcase())

print("hellO WOrLd".title())

print("abraca dabra".upper())

str1 = "this is string example....wow!!!"
print ("str.zfill : ",str1.zfill(40))
print ("str.zfill : ",str1.zfill(50))







