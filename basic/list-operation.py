list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list1[3]=2004

print("New value of list1[3]:",list1[3])

list1.append('2020')
print(list1)

del list2[3]
print(list2)

print(len(list2))

print(list1+list2)

print(['Hi']*4)

print("3 in list2:",3 in list2)

for x in list1:
    print(x,end=' ')


L=['C','C++','Java','Python']

print(L[1])

print(L[2:])

print(L[-2])

marks=[45,78,90,22,87,45]

print("Max:",max(marks))

print("Min:",min(marks))

t=('python','java','c')

print(list(t))


li=[45,87,33,46,9]

print(li.sort())

print(li.reverse())

print(li.remove(45))

print(li.append(99))

print(li.pop())

li.insert(2,100)

print(li)

li.extend(list1)

print(li)

