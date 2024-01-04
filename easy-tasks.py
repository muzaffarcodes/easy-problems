# 1 

a = 12
b = 23
a1,b1 = b,a
print("a =",a1)
print("b =",b1)

# 2

a = int(input("Son: "))
b = str(a)
print(b[::-1])

# 3

string = 'saud_abdulwahed'
print(string[::-1])

# 4

list1 = [2,33,5,6,7,8654,3,32,45,2.2,11]
print(list1[::-1])

# 5 

list2 = [12,24,2,4,6,7,8,12,24,24]
print(list2.count(24))

# 6

even = lambda num1 : num1 % 2 == 0
if(even(19)):
	print("Juft")
else:
	print("Toq")

# 7

son1 = int(input("Son1: "))
son2 = int(input("Son2: "))

natija = abs(son1)-(-(son2))
print(natija)

# 8

for i in range(12):
	print(i * '*')

# 9 

fb = [0,1,1,]
x = 1
y = 1

for i in range(10):
    z = x + y
    x = y
    y = z
    fb.append(z)

faylnomi = "fibonaci1.txt"
with open(faylnomi, "w") as fayl:
    fayl.write(f"{fb}")
    
n = int(input("n-fibonachi sonini toping:"))
print("{} - fibonachi soni =  {}".format(n,fb[n-1] + fb[n-2]))

print("")
a = 0
for i in fb:
    print(f"{a}-son: {i}")
    a += 1

print("{} - fibonachi soni =  {}".format(n,fb[n-1] + fb[n-2]))

# 10

import random
list_matrix = [[],[],[],]
for i in range(3):
	for j in range(3):
		list_matrix.append(random.randint(0,9))
print("Matrix: \n")

for i in list_matrix:
	print(i)	

start = list_matrix[0][0] + list_matrix[1][1] + list_matrix[2][2]
stop = list_matrix[2][0] + list_matrix[1][1] + list_matrix[0][2]
abs_qiymat = abs(start-stop)
print(f"Absolyut qiymat: {start} - {stop} = {abs_qiymat}")

# 11
list3 = [11,42,52,23,20,0]
print(sorted(list3))

list3 = [11,42,52,23,20,0]
list3.sort()
print(list3)

list3 = [11,42,52,23,20,0]
list3.sort(reverse=False)
print(list3)

# 12

def read_num(number):
	dict = {1:"o'n",2:"yigirma",3:"o'ttiz",4:"qirq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"to'qson"}
	dict1 = {1:"bir",2:"ikki",3:"uch",4:"to'rt",5:"besh",6:"olti"}






