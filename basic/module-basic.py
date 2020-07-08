import fib

print(fib.fibonacci(100))

Money = 2000
def AddMoney():
   global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)

content=dir(fib)
print(content)


hello='90'
if 'hello' in locals():
    print('hello is there!!!')

