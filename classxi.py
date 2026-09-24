#PREETI ARORA - CLASS 11


# Removed `curses` import (not available on Windows).
# Use the built-in string method `str.isspace()` instead.

print('hello world')

def func1(): #func
    print('i am learning functions in python')
func1()

def triangle(): #func
    print('i am learning triangle in python')
triangle()

def areaRectangle(length,breadth): #func
    area=length*breadth
    return area
result = areaRectangle(10,20)
print(result)

grade=input('enter your grade:') #if-elif-else
if grade=='A':
    print('excellent')
elif grade=='B':
    print('good')
elif grade=='C':
    print('average')
else:
    print('invalid grade')

for character in 'character': #for-loop
    print(character)
else:
    print('loop is completed')

for n in range(5):  #number-print
    print(n*10)

counter=0 #while-loop
while counter <3:
    print('inside while loop')
    counter+=1

i=2                         #pattern1
while (i>=0):
    j=2
    while (j>=0):
        print(2,end=' ')
        j-=1
    print()
    i=i-1

for i in range(1,6):         #pattern2
    for j in range(1,i+1):
        print(j,end=' ')
    print()

entry=0
sum=0
print("enter numbers to sum, negative numbers ends list:")  #sum-of-numbers
while True:
    entry=eval(input())
    if entry<0:
        break
    sum+=entry
print("sum of numbers is:",sum)

for val in "string":
    if val=="i":
        continue
    print(val)
print("the end")

#working of a pass statement

sequence=['p','a','s','s']
for val in sequence:
    pass    #null operation, nothing happens when it executes

print("enter your name:")   #string -> immutable
name=input()
print("hello " + name)

var="hello world" #0->-11
print(var[-1])

str="hello world"
for i in str:
    print(i)

str1="hello world"
index=0
while index<len(str1):
    print(str1[index])
    index+=1

str=input("enter a string: ")     #string-traversal
ch=input("enter the characters to be searched: ")
count=0
for character in str:
    if character==ch:
        count+=1
print("number of times character ",ch," occurs in the string is: ",count)

str=input("enter a string:")    #reverse-string
for i in range(-1,-len(str)-1,-1):
    print(str[i],end='')

print(3*'\nhello world\n') #string-replicate
print(2*'2')
str="\npython\n"
print(str*3)

print('H' in 'HELLO') #membership operators
print('h' in 'HELLO')
print('h' not in 'hello')
str1='my'
string='my book'
print(str1 in string)

alphabet_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"    #string-slicing-> start:end:step
sliced_string=alphabet_string[6:15:2]
print(alphabet_string)
print(sliced_string)

#methods:
#len()-returns length of string
#capitalize()-returns the exact copy of the string with the first letter in uppercase
#split()-breaks up a string at the specified seperator and returns a list of substrings
    #seprator() and maxsplit() // default value for maxsplit is -1: no limit on no. of splits

str1=input("enter a string: ")
print("original_string: ",str1)
str2=""
x=str1.split()
for a in x:
    str2+=a.capitalize()+" "
print(str2)

grocery='Red:Blue:Orange:Pink'
print(grocery.split(':',2))

#replace()-replaces all occurances of old string with new string
str1="this is a string"
print(str1.replace("is","was"))

#find()-serach the first occurrence of a substring in a given string
word="green revolution"
result=word.find("green")
print(result)
result1=word.find("Green")
print(result1)
result2=word.find("e",4)
print(result2)
result3=word.find("en",5)
print(result3)
result4=word.find("o",11,14)
print(result4)

#isalpha()-checks for alphabets in an inputted string. returns TRUE/FALSE
str1="good"
print(str1.isalpha())
str2="this is a string"
print(str2.isalpha())

#isdigit()-returns TRUE if the string contains only digits orelse FALSE
str1="12345"
print(str1.isdigit())
str2="ram is a good boy"
print(str2.isdigit())

#lower()-converts all uppercase letters in the string into lowercase
str1="LEARN PYTHON"
print(str1.lower())

#islower()-returns true if all the characters in the string are in lowercase
str1="learn python"
print(str1.islower())

#upper()-converts all lowercase letters in the string into uppercase
str1="learn python"
print(str1.upper())

#isupper()-returns true if all the characters in the string are in uppercase
str1="LEARN PYTHON"
print(str1.isupper())

#lstrip()-removes all the leading whitespaces in the string
str1="  hello world  "
print(str1.lstrip())

#rstrip()-removes all the trailing whitespaces in the string //rstrip(chars)-removes all the trailing characters in the string
str1="  hello world  "
print(str1.rstrip())

#strip()-removes all the leading and trailing whitespaces in the string
str1="  hello world  "      
print(str1.strip())

#isspace()-returns true if the string contains only whitespace characters orelse false
str1="   "
print(str1.isspace())

#istitle()-returns true if the first character of each word in the string is in uppercase orelse false
str1="This Is A String"
print(str1.istitle())

#join(sequence)-returns a string which is the concatenation of the strings in the sequence
str1=" "
print(str1.join(["hello","world"]))

#startswith()-returns true if the string starts with the specified prefix orelse false
str1="hello world"
print(str1.startswith("hello"))

#endswith()-returns true if the string ends with the specified suffix orelse false
str1="hello world"  
print(str1.endswith("world"))

#swapcase()-converts all uppercase letters in the string into lowercase and vice versa
str1="Hello World"
print(str1.swapcase())

#partition(Separator)-returns a tuple containing the part before the separator, the separator itself and the part after the separator
str1="hello world"
print(str1.partition(" "))

#ord()-returns the unicode code point for a given character
print(ord("a"))

#chr()-returns the character that represents the specified unicode code point
print(chr(97))

my_list=[10,20,30,40,50] #list
print(my_list)

my_list=["deep",450,True,3.14]
print(my_list)

list1=[10,[20,30,40],50]
print(list1)

list1=list("computer")
print(list1)

list1=list()
print(list1)
print(type(list1))

dob="1998-08=12"
print(list(dob))

list1=[10,20,30,40,50] #list-indexing
print(list1[0])
print(list1[2])

list1=list(input("enter values: "))
print(list1)

#accessing list elements using negative indexing
list1=[10,20,30,40,50] 
print(list1[-1])

#accessing list elements using slicing
list1=[10,20,30,40,50]
print(list1[1:4])

#accessing list elements using slicing with step
list1=[10,20,30,40,50]
print(list1[0:5:2])

#traversing a list using for loop
list1=[10,20,30,40,50]
for i in list1:
    print(i)

#traversing a list using range() func and len() func
list1=[10,20,30,40,50]
for i in range(len(list1)):
    print(list1[i])

#aliasing in lists
list1=[10,20,30,40,50]
list2=list1
print(list2)

#concatenation of lists
list1=[10,20,30]
list2=[40,50,60]
list3=list1+list2
print(list3)

#repetition of lists ,   NO list*list
list1=[10,20,30]
list2=list1*3
print(list2)

#membership operators in lists
list1=[10,20,30,40,50]
print(20 in list1)
print(60 not in list1)

#index() method in lists
list1=[10,20,30,40,50]
print(list1.index(30))
print(list1[2])
print(list1[-1])

#slice() method in lists
list1=[10,20,30,40,50]
print(list1[1:4])

#appending elements to a list using append() method
list1=[10,20,30]
list1.append(40)
print(list1)

#write a program to find the second largest number in a list 'Num'
print("enter the number of elements in the list:")
n=int(input())
i=0
Num=[]
while i<n:
    print("enter the element:")
    ele=int(input())
    Num.append(ele)
    i+=1
print("the original list is:",Num)
for i in range(n):
    print(Num[i],end=' ')
if (Num[0]>Num[1]):
    first=Num[0]
    second=Num[1]
else:
    first=Num[1]
    second=Num[0]
for x in Num[2:]:
    if x > second:
        if x > first:
            second = first
            first = x
        else:
            second = x
print("the second largest number is:", second)

#adding elements in a list
def main():
    l=[]
    n=int(input("enter the number of elements in the list:"))
    i=1
    while i<=n:
        ele=int(input("enter the element:"))
        l.append(ele)
        i+=1
    print(l)

#extend()
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
print(l1)

#insert()
l1=[10,20,30]
l1.insert(1,15)
print(l1)

#reverse()
l1=[10,20,30]
l1.reverse()
print(l1)

#index()
l1=[10,20,30]
print(l1.index(20))

#updating list
l1=[10,20,30]
l1[1]=25    
print(l1)

#len()
l1=[10,20,30]
print(len(l1))  

#sort()
l1=[30,10,20]
l1.sort()
print(l1)

#clear()
l1=[10,20,30]
l1.clear()
print(l1)

#count()
l1=[10,20,30,10,20,10]
print(l1.count(10))

#deletion operations in lists
l1=[10,20,30]
del l1[1]
print(l1)

#del()
l1=[10,20,30]
del l1[1]
print(l1)

#remove()
l1=[10,20,30]
l1.remove(20)
print(l1)

#del() using slice
l1=[10,20,30,40,50]
del l1[1:4]
print(l1)

#write a program to delete all odd numbers and negative numbers from list
l1=[10,20,30,40,50,-1,-2,-3]
len1=len(l1)
i=0
while i<len1:
    if (l1[i]<0):
        del l1[i]
        len1-=1
        i-=1
    elif (l1[i]%2!=0):
        del l1[i]
        len1-=1
        i-=1
    i+=1
print(l1)

#count the occurance of a number in a list
l1=[10,20,30,10,20,10]
num=eval(input("enter the number to be counted:"))
count=0
for i in l1:
    if i==num:
        count+=1
print("the number of times",num,"occurs in the list is:",count)

#linear search in a list
l1=eval(input("enter the list elements:"))
length=len(l1)
element=int(input("enter the element to be searched:"))
for i in range(0,length):
    if element==l1[i]:
        print(element , "the element is found at index:", i)
        break
else:
    print(element , "is not found in the list")

#split original list into 2 separte lists
l1=['Mon',45,'Tue',43,'Wed',42,'Thu',40,'Fri',38,'Sat',40,'Sun',38]
len1=len(l1)
days=[]
temp=[]
for i in range(len1):
    if (i%2==0):
        days.append(l1[i])
    else:
        temp.append(l1[i])
print("the days are:",days)
print("the temperature are:",temp)
print("the original list is:",l1)

#menu driven program to do various list operations
l1=[22,4,16,38,13]
choice=0
while True:
    print("the list has the following elements:",l1)
    print("\n L I S T  O P E R A T I O N S :")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to the existing list")
    print("4. Modify an existing element in the list")
    print("5. Delete an existing element by its position")
    print("6. Delete an existing element by its value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")
    choice=int(input("enter your choice(1-10):"))
    if choice==1:
        ele=int(input("enter the element to be appended:"))
        l1.append(ele)
        print("the element is appended successfully")
    elif choice==2:
        pos=int(input("enter the position where the element is to be inserted:"))
        ele=int(input("enter the element to be inserted:"))
        l1.insert(pos,ele)
        print("the element is inserted successfully")
    elif choice==3:
        n=int(input("enter the number of elements in the list to be appended:"))
        l2=[]
        for i in range(n):
            ele=int(input("enter the element:"))
            l2.append(ele)
        l1.extend(l2)
        print("the list is appended successfully")
    elif choice==4:
        pos=int(input("enter the position of the element to be modified:"))
        ele=int(input("enter the new value of the element:"))
        l1[pos]=ele
        print("the element is modified successfully")
    elif choice==5:
        pos=int(input("enter the position of the element to be deleted:"))
        del l1[pos]
        print("the element is deleted successfully")
    elif choice==6:
        ele=int(input("enter the value of the element to be deleted:"))
        l1.remove(ele)
        print("the element is deleted successfully")
    elif choice==7:
        l1.sort()
        print("the list is sorted in ascending order")
    elif choice==8:
        l1.sort(reverse=True)
        print("the list is sorted in descending order")
    elif choice==9:
        print("the list is:", l1)
    elif choice==10:
        break
    else:
        print("invalid choice")
        print("\n\nPress any key to continue...")
        ch=input()

#bubble sort
def main():
    l1=[22,4,16,38,13]
    n=len(l1)
    print("the original list is:",l1)
    for i in range(n-1):
        for j in range(n-i-1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    print("the sorted list is:",l1)

#create an integer list and sort the list in ascending order using bubble sort
l1=[22,4,16,38,13]
ch='y'
n2=1
print("enter the list elements:")
while ch=='y' or ch=='Y':
    print("element",n2,":")
    ele=int(input())
    l1.append(ele)
    #n2+=1
    ch=input("do you want to enter more elements?(y/n):")
    if ch=='n' or ch=='N':
        break
    else:
        n2+=1
l1.append(0)
ctr=i=0
n=len(l1)
print("the original list is:",l1)
for i in range(0,n):
    print(l1[i],end=' ')
for i in range(n):
    for j in range (n-1):
        if l1[j] > l1[j+1]:
            ctr+=1
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print()
print("the sorted list")
for i in range(0,n):
    print(l1[i],end=' ')
print("the total no of passes:",ctr)

#insertion sort
a=[22,4,16,38,13]
print("the original list is:",a)
for i in a:
    j=a.index(i)
    while j>0:
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
        else:
            break
        j=j-1
print("the sorted list is:",a)

#write a program to shift each element of the list to the right and 
# the last element will be moved to the first position
l1=[10,20,30,40,50]
temp=l1[len(l1)-1]
for i in range(len(l1)-1, -1, -1):
    l1[i] = l1[i-1]
l1[0] = temp
print("the shifted list is:", l1)

#tuples
t1=(10,20,30,40,50)
tup=10,20,30
tup1=()
tup2=('hello',1,5,6,'python')
tup3=((10,20,30),('hello','world'))
tup4=tuple('python')
tup5=([1,2,3],['a','b','c'])
t2=(10,)
print(type(t2))

#tuple creation using tuple() constructor
tup1=tuple()
print(tup1)
tup2=tuple('python')
print(tup2)

#creating tuple using while loop
t=tuple()
n=int(input("enter the number of elements in the tuple:"))
i=1
while (i<=n):
    ele=input("enter the element:")
    t+=(ele,)
    i+=1
print("the created tuple is:",t)

#creating tuple using for loop
t=tuple()
n=int(input("enter the number of elements in the tuple:"))
for i in range(n):
    ele=input("enter the element:")
    t+=(ele,)
print("the created tuple is:",t)

#'n' number of elements in a tuple
t=tuple()
n=int(input("how many elements?:"))
print("enter the elements:")
for i in range(n):
    ele=input("enter the element:")
    t+=(ele,)
print("the created tuple is:",t)

#program to store records of students in a tuple
st=((200,"ram",20), (201,"shyam",21), (202,"mohan",22))
print("S_No", "Name", "Age", "Marks")
for i in range(0,len(st)):
    print((i+1), st[i][1], st[i][2], st[i][0])

#tuple indexing start at 0
t1=(10,20,30,40,50,60,70,80,90,100)
print("the first element of the tuple is:", t1[0])
print("the second element of the tuple is:", t1[1])
print("the third element of the tuple is:", t1[2])

#using in operator in loop
tup=('p','y','t','h','o','n')
for i in tup:
    print(i)

#using range() function
tup=('p','y','t','h','o','n')
n=len(tup)
for i in range(n):
    print(tup[i])

#tuple slicing
tup=('p','y','t','h','o','n')
print("the sliced tuple is:", tup[1:4])

#in and not membership operators in tuples
tup=('p','y','t','h','o','n')
print('y' in tup)

#tuple concatenation
tup1=('p','y','t')
tup2=('h','o','n')
tup3=tup1+tup2
print("the concatenated tuple is:",tup3)

#tuple multiplication
tup1=('p','y','t')
tup2=tup1*3
print("the multiplied tuple is:",tup2)

#any() and all() functions in tuples
tup1=(0,1,2,3)
print(any(tup1))
tup2=(1,2,3,4)
print(all(tup2))

#min() and max() functions in tuples
tup1=(10,20,30,40,50)
print("the minimum value in the tuple is:",min(tup1))
print("the maximum value in the tuple is:",max(tup1))

#comparing tuples
tup1=(10,20,30)
tup2=(10,20,30)
if tup1==tup2:
    print("the tuples are equal")

#program to input numbers in tuples and find min and max
tup=()
n=int(input("enter the number of elements in the tuple:"))
for i in range(n):
    ele=int(input("enter the element:"))
    tup+=(ele,)
print("the created tuple is:",tup)
print("the minimum value in the tuple is:",min(tup))        
print("the maximum value in the tuple is:",max(tup))        

#deleting a tuple
tup=(10,20,30,40,50)
del tup
print("the tuple is deleted successfully")

#write a program to input any two tuples and swap their elements
tup1=()
tup2=()
n=int(input("enter the number of elements in the first tuple:"))
for i in range(n):
    ele=int(input("enter the element:"))
    tup1+=(ele,)
n=int(input("enter the number of elements in the second tuple:"))
for i in range(n):
    ele=int(input("enter the element:"))
    tup2+=(ele,)
print("the first tuple is:",tup1)
print("the second tuple is:",tup2)
#swapping the tuples
tup1,tup2=tup2,tup1
print("after swapping:")
print("the first tuple is:",tup1)
print("the second tuple is:",tup2)

#DICTAIONARY IN PYTHON
d={"name":"ram","age":20,"marks":80}
print(d)
d={}

#write a program to input total number of sections and stream name in 11th standard nd display
#all info on output screen using dictationary
classxi=dict()
n=int(input("enter the total number of sections in 11th standard:"))
i=1
while i<=n:
    a=input("enter the section name:")
    b=input("enter the stream name:")
    classxi[a]=b
    i+=1
print("classes",'\t',"section",'\t',"stream name")
for i in classxi:
    print ("xi",'\t',i,'\t',classxi[i])
    
#write a program to store info about students in a dict and display info based on admission no
scl=dict()
i=1
flag=0
n=int(input("enter the number of entries:"))
while i<n:
    adm=input("\nenter admission no of a student:")
    nm=input("enter name of the student:")
    sec=input("enter class and section")
    per=float(input("enter percentage of a student"))
    b=(nm,sec,per)
    scl[adm]=b
    i=i+1
l=scl.keys()
for i in l:
    print("\nadmno ",i," :")
    z=scl[i]
    print("Name\t","class\t","per\t")
    for j in z:
        print(j,end="\t")

#program to create a dictationary with names of employees and their salary
num=int(input("enter the number of employees whose data to be stored:"))
count=1
employee=dict()
while count<=num:
    name=input("enter the name of the employees:")
    salary=int(input("enter the salary:"))
    employee[name]=salary
    count=count+1
print("\nemployee_name\tsalary")
for k in employee:
    print(k,'\t\t',employee[k])

#program to count the number of times a character appears in a given string
str=input("enter a string:")
dict1={}
for ch in str:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1
for key in dict1:
    print(key,':',dict1[key])

#introduction to modules: examples: 
#first create a file and name it area.py
#import math
#def circle_area(radius):
    #return math.pi*radius*radius
#def square_area(side):
    #return side*side
#def rectangle_area(length,breadth):
    #return length*breadth
#now create another file " math1.py"
#import area
#print(area.circle_area(5))
#print(area.rectangle_area(10,5))
#print(area.square_area(5))
#dir(area)
#from area import circle_area
#print (circle_area(10))
#from area import *
#print(area.circle_area(5))
#print(area.rectangle_area(10,5))
#print(area.square_area(5))

#Create following tuple of tuples by accepting each color as input from user. Now write a function to 
#check whether a color accepted from user exist in that tuple color using a suitable method of tuple.
#colors = (
# ('Red', 'White', 'Blue'),
# ('Green', 'Pink', 'Purple'),
# ('Orange', 'Yellow', 'Lime'),
#)
def check_color(colors, color):
    for group in colors:
        if color in group:
            return True
    return False
colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
search = input("Enter a color to search: ")
if check_color(colors, search):
    print(search, "exists in the tuple.")
else:
    print(search, "does not exist in the tuple.")

#Create a list of tuples 'lst_tuples' containing tuples of integers
#lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#and convert each tuple in 'lst_tuples' to a list using list comprehension and print it.
lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
list_result = [list(item) for item in lst_tuples]
print("Original Tuple List:")
print(lst_tuples)
print("\nConverted List:")
print(list_result)

#Say you have a tuple as follows :
#tuple1 = (2, 7, [5,7,8], 'Tutor' , True, 'T', 3.21 ) # different data types
#Write a function to remove 2nd element and last item from the tuple assuming you don’t know the 
#index of last element and print the original tuple and resultant tuple after removing operation and 
#corresponding ids
def remove_items(t):
    print("Original Tuple :", t)
    print("Original ID :", id(t))
    new_tuple = t[:1] + t[2:-1]
    print("\nNew Tuple :", new_tuple)
    print("New ID :", id(new_tuple))
tuple1 = (2, 7, [5, 7, 8], 'Tutor', True, 'T', 3.21)
remove_items(tuple1)

#Say you have a tuple nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
#Write a function which will return a list of the average of 1st item of each inner tuple, the average of 
#the 2nd item of each inner tuple and the average of the 3rd item of each inner tuple using list 
#comprehension
def averages(nums):
    return [sum(item[i] for item in nums) / len(nums) for i in range(len(nums[0]))]
nums = (
    (1, 1, -5),
    (30, -15, 56),
    (81, -60, -39),
    (-10, 2, 3)
)
print("Averages:")
print(averages(nums))

#You have stored 12 months’ salary in a tuple like 
#monthly_incomes = ( ("January", 5000), ("February", 5500), 
# ("March", 6000), ("April", 5800),
# ("May", 6200), ("June", 7000), 
# ("July", 7500), ("August", 7300),
# ("September", 6800), ("October", 6500),
# ("November", 6000),("December", 5500) )
#generate following report 
'''using monthly_Incomes:
Total income : 75100
 January: 5000
 February: 5500
 March: 6000
--------------------
 Quarter: 16500
 April: 5800
 May: 6200
 June: 7000
--------------------
 Quarter: 19000
 July: 7500
 August: 7300
 September: 6800
--------------------
 Quarter: 21600
 October: 6500
 November: 6000
 December: 5500
--------------------
 Quarter: 18000'''
monthly_incomes = (
    ("January", 5000),
    ("February", 5500),
    ("March", 6000),
    ("April", 5800),
    ("May", 6200),
    ("June", 7000),
    ("July", 7500),
    ("August", 7300),
    ("September", 6800),
    ("October", 6500),
    ("November", 6000),
    ("December", 5500)
)
total_income = sum(income for month, income in monthly_incomes)
print("Total Income :", total_income)
print()
quarter_total = 0
for i, (month, income) in enumerate(monthly_incomes, start=1):
    print(f"{month}: {income}")
    quarter_total += income
    if i % 3 == 0:
        print("--------------------")
        print("Quarter:", quarter_total)
        print()
        quarter_total = 0

#Write two functions to check sentence palindrome and number palindrome. 
#Some example of palindrome sentences :
#1. A man, a plan, a canal — Panama! 
#2. rotator.
#3. deed.
#4. A nut for a jar of tuna.
#5. Go dog!
#6. Don't nod.
#7. No lemon, no melon.
#8. Was it a car or a cat I saw?
#9. Oozy rat in a sanitary zoo.
#10. Never odd or even.
#We can run the code and use above sentences or number to check the palindrome
# Function to check sentence palindrome
def sentence_palindrome(sentence):
    clean = ""
    for ch in sentence:
        if ch.isalnum():
            clean += ch.lower()
    if clean == clean[::-1]:
        return True
    else:
        return False
# Function to check number palindrome
def number_palindrome(num):
    return str(num) == str(num)[::-1]
# Driver Program
sentence = input("Enter a sentence: ")
if sentence_palindrome(sentence):
    print("Sentence is Palindrome")
else:
    print("Sentence is Not Palindrome")
num = int(input("Enter a number: "))
if number_palindrome(num):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")

#Generate following output by iterating the range 100-200 after checking each for prime and sum 
#of digits is an even number.
#Output :
#100 is not prime and sum of digit is not even
#101 is prime and sum of digit is even
#102 is not prime and sum of digit is not even
#103 is prime and sum of digit is even
#104 is not prime and sum of digit is not even
#105 is not prime and sum of digit is even …………
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def even_digit_sum(n):
    s = sum(int(d) for d in str(n))
    return s % 2 == 0
for i in range(100, 201):
    prime = "prime" if is_prime(i) else "not prime"
    even = "even" if even_digit_sum(i) else "not even"
    print(f"{i} is {prime} and sum of digit is {even}")

#Write a function which will take a list of numbers as parameter and return following information 
#as a list after analyzing the input list.  
#Sum of all Numbers 
#Sum of all Odd Numbers 
#Sum of all Even Numbers  
#Count of Odd Numbers  
#Count of Even Numbers 
#List of Even Numbers 
#List of odd numbers
def analyze_list(lst):
    total = sum(lst)
    even_list = [x for x in lst if x % 2 == 0]
    odd_list = [x for x in lst if x % 2 != 0]
    result = [
        total,
        sum(odd_list),
        sum(even_list),
        len(odd_list),
        len(even_list),
        even_list,
        odd_list
    ]
    return result
numbers = [10, 5, 12, 9, 8, 7, 20]
answer = analyze_list(numbers)
print("Sum of all Numbers =", answer[0])
print("Sum of Odd Numbers =", answer[1])
print("Sum of Even Numbers =", answer[2])
print("Count of Odd Numbers =", answer[3])
print("Count of Even Numbers =", answer[4])
print("Even Numbers =", answer[5])
print("Odd Numbers =", answer[6])

#1. Write a Python program to find the roots of a quadratic equation.
#2. Write a Python program to check leap year.
#3. Write a Python program to find the nth term in a Fibonacci series using recursion
#4. Interchange first and last elements in a list using various approaches (at least four approach)

import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", r1, "and", r2)
elif d == 0:
    r = -b / (2*a)
    print("Equal Roots:", r)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Roots are:")
    print(real, "+", imag, "i")
    print(real, "-", imag, "i")

year = int(input("Enter Year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter n: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

lst = [10, 20, 30, 40, 50] #temp variables
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print(lst)
lst = [10, 20, 30, 40, 50] #tupple swapping
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
lst = [10, 20, 30, 40, 50] #using pop and insert
first = lst.pop(0)
last = lst.pop(-1)
lst.insert(0, last)
lst.append(first)
print(lst)
lst = [10, 20, 30, 40, 50] #using slicing
lst = [lst[-1]] + lst[1:-1] + [lst[0]]
print(lst)

#module aliasing
#create a file named test.py
'''
x=100
def add(a,b):
    print("the sum is :",a+b)
def product(a,b):
    print("the product is :",a*b)
'''
#then create another file named prog_test1.py
'''
import test
print(test.x)
test.add(10,20)
test.product(10,20)
'''
#then create another file names prog_test2.py where modify the above program by using alias 
#name for the module test
'''
import test as m
print(m.x)
m.add(10.20)
m.product(10,20)
'''

#member aliasing
#prog_test3.py
'''
from text import x as p,add as sum
print (p)
sum(100,200)
'''

#circle.py
'''
import math
def area(radius):
    return math.pi*radius**2
def circumference(radius):
    return 2*math.pi*radius
'''
#rectangle.py
'''
def area(width,length):
    return width * length
def perimeter(width,length):
    return 2*(width+length)
'''
#prog_mod_alt1.py
'''
import circle
import rectangle
choice=0
ch="y"
while(ch=="y"):
    print("MENU ")
    print("1. area of the circle")
    print("2. circumference of the circle")
    print("3. area of the rectangle")
    print("4. perimeter of the rectangle")
    print("5. quit")
    choice==int(input("enter your choice:"))
    if(choice==1):
        radius=int(input("enter the circles radius"))
        print("the area is",circle.area(radius))
    elif(choice==2):
        radius=int(input("enter the circles radius"))
        print("the circumference is",circle.circumference(radius))
    elif(choice==3):
        radius=int(input("enter the circles radius")) //rectangle
        print("the area is",circle.area(radius))
    elif(choice==4):
        radius=int(input("enter the circles radius"))  //rectangle
        print("the area is",circle.area(radius))
    elif(choice==5):
        print("exit")
    else:
        print("invalid")
'''


#random module
import random
random.randrange(30)

#to select a random subject
import random
subjects=["computer science","maths","physics","accounting"]
ran_index=random.randrange(2)
print(subjects[ran_index])

#random()
from random import random
print(random())

from random import random
n=random()*900+100
n=int(n)
print(n)

a=n//100
b=(n//10)%10
c=n%10
print(a+b+c)

import random
print(random.randint(0,9))

#a func that fills a list with numbers using randint()
from random import randint
def fill_list(lst,limit_num,low,high):
    for i in range(limit_num):
        lst.append(random.randint(low,high))
minimum=int(input("min : "))
maximum=int(input("max : "))
n=int(input("numbers limit: "))
a=[]
fill_list(a,n,minimum,maximum)
print(a)

#calculate mean of floating values in a list
def cal_mean(list1):
    total=0
    count=0
    for i in list1:
        total = total+i
        count = count+1
    mean=total/count
    print("the calculated mean is :", mean)

list1=[2.6,3.4,8.5,7.9]
cal_mean(list1)