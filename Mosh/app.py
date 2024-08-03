"""
https://www.youtube.com/watch?v=kqtD5dpn9C8
# exercise #1

# age = 20
msg = "this is from mosh tutorial in youtube"
print("msg" + msg)
print("age" + str(age))

# exercise #2

name = input("what is your name? ")
print("welcome "+ name)

# exercise #3

first_num = float(input("First number: "))
second_num = input("Second number: ")
Sum = first_num + float(second_num)

print("The sume is: " + str(Sum))

# exercise #4

course ="python for begineers"
print(course.upper())
print(course)
print(course.replace('for', '4' ))
print(course.find("for")) # gives index
print("for" in course) # gives true/false

# exercise #5

print(10//2)
print(10%3)
print(10**3) #power of 
z=3
z+=5
print(z+3)

#exercise #6

price = 25
print(price >10 and price < 30)
print(price >10 or price >30)
print(not price > 10)

#exercise #7

temp = 35
#python doesnt have {} braces
if temp >40:
    print("It's is a hot day")
    print('second line')
elif temp >30:
    print("its nice day")
elif temp>10:
    print("its cold")
else:
    print("else line")

#exercise #8

weight = input("Weight: ")
unit = input("Kg or Lbs : ")
if unit.upper() == 'K':
    convert =float(weight)/0.45
    print ("weight in Lbs is " + str(convert))
else:
    convert = float(weight)*0.45
    print("Weight in Kgs is " + str(convert))
    
#exercise #9

i = 1
while(i<2):
    print(i)
    i+=1
while(i<5):
    print(i * '*')
    i+=1


#exercise #10
names = ['john', 'mash','mmill','kavi']
names[0] = 'jognh'
print(names)
print(names[-1]) # prints kavi
print(names[0:3])
# print(names[0].upper)

#exercise #11
# for loop > while loop
num =[1,2,3,5,4,6,5,7,5]
for item in num:
    print(item)

#exercise #12
numbers = range(4,10)
for num in numbers:
    print(num)

num2 = range(0,10,2) # step function
for num in num2:
    print(num)
"""

#exercise #13
num1 =[1,2,3] #lists
num2 =(1,2,3) #tuples -> immutable
print(num1)
print(num2)