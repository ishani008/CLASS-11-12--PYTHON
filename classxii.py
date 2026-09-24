#PREETI ARORA 
#SUMITA ARORA

#.PY- PYTHON SOURCE FILE
#.PYC- COMPILED BYTECODE FILE
#.PYD- COMPILED DLL FILE
#.PYO- OPTIMIZED BYTECODE FILE
#.PYW- PYTHON SOURCE FILE FOR WINDOWS
#.PYZ- COMPRESSED PYTHON SOURCE FILE//SCRIPT ARCHIVE

#math modules - ceiling, floor, trunc, sqrt, pow, exp, log, log10, sin, cos, tan, radians, degrees , help , random, choice, shuffle, 
#               randint, uniform, seed, time, factorial, gcd, lcm

###MAIN MODULE###

def areaRectangle(l,b=1):
    area = l * b
    return area
def main():
    print('enter length and breadth of rectangle:')
    l = int(input('enter length: '))
    b = int(input('enter breadth:'))
    areaRect=areaRectangle(l, b)
    print('area of rectangle:', areaRect)
if __name__ == '__main__':
    main()

###RECURSION###

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
a=2
print('power of',a,'is:',power(a,3))

#func to find sum of n natural numbers

def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)
num=int(input('enter a number:'))
if num<0:
    print('enter a positive number')
else:
    print('sum of natural numbers up to', num, 'is:', recur_sum(num))

#FUNC TO FIND FACTORIAL OF A NUMBER

def recur_factorial(n):
    if n==1:
        return n
    else:
        return n * recur_factorial(n-1)
num=int(input('enter a number:'))
if num<0:
    print('enter a positive number')
elif num==0:
    print('factorial of 0 is 1')
else:
    print('factorial of', num, 'is:', recur_factorial(num))

#func to find fibonacci series

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
nterms=int(input('enter number of terms:'))
print('fibonacci series:')
for i in range(nterms):
    print(recur_fibo(i))

#PROGRAM FOR BINARY SEARCH IN A LIST/ARRAY USING RECURSION

def binary_search(arr, low, high, target):
    if high < low:
        return None
    else:
        mid = (low + (high-low)) // 2
        if arr[mid] > target:
            return binary_search(arr, low, mid-1, target)
        elif arr[mid] < target:
            return binary_search(arr, mid+1, high, target)
        else:
            return mid
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(list1, 0, len(list1)-1, 5))

#python built in mathematical functions - math.ceil(), math.floor(), math.trunc(), math.sqrt(), math.pow(), math.exp(), math.log(), math.log10(),
#                                         math.sin(), math.cos(), math.tan(), math.radians(), math.degrees(), help(math), random.choice(), 
#                                         random.shuffle(), random.randint(), random.uniform(), random.seed(), random.time(), 
#                                         math.factorial(), math.gcd(), math.lcm() , math.isqrt(), math.isclose(), math.isfinite(), 
#                                         math.isinf(), math.isnan(), math.copysign(), math.fabs(), math.fmod(),
#                                         math.frexp(), math.ldexp(), math.modf(), math.remainder(), math.e(), 
#                                         math.pi(), math.tau(), math.inf(), math.nan(), math.dist(), math.hypot(), 
#                                         math.prod(), math.comb()

from math import tan, pi
from random import choice
from random import choice
import struct
no_sides = int(input('enter number of sides of polygon:'))
length = float(input('enter length of side:'))  
polygon_area = (no_sides * length ** 2) / (4 * tan(pi / no_sides))
print('area of polygon:', polygon_area)

#program to find the root of a quadratic equation using math.sqrt() function
import math
a = float(input('enter coefficient of x^2:'))
b = float(input('enter coefficient of x:'))
c = float(input('enter constant term:'))
d = (b ** 2) - (4 * a * c)
if d < 0:
    print('roots are imaginary')
elif d > 0:          #r>0
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print('the roots are:', root1, 'and', root2)
else:          #r=0
    root1 = root2 = -b / (2 * a)
    print('the roots are:', root1, 'and', root2)

#program to calculate arc length of an angle
import math
def arc_length():
 diameter=float(input('enter diameter of circle:'))
 angle=float(input('enter angle in degrees:'))
 if angle>=360:
    print('angle should be less than 360 degrees')
 else:
    radius = diameter / 2
    arc_length = radius * math.radians(angle)
    print('arc length:', arc_length)
arc_length()

#python program to convert a binary number to decimal number using math.pow() function
import math
binary_num = input('enter a binary number:')
decimal_num = 0
for i in range(len(binary_num)):
    digit=binary_num[-(i + 1)] #pops the last digit of the binary number
    if digit=='1':
        decimal_num += math.pow(2, i)
print('decimal number:', decimal_num)

#python function that takes a list of words and returns the length of the longest one using math module
def longest_word_length(words_list):
    word_len=[]
    for n in words_list:
        word_len.append((len(n),n))
        word_len.sort()
    return word_len[-1][1]
print('length of longest word:', longest_word_length(['python', 'java', 'c++', 'javascript']))

#python program to capitalize first and last letters of a string using math module
import math
def capitalize_first_last(string):
    if len(string) < 2:
        return string.upper()
    else:
        first_letter = string[0].upper()
        last_letter = string[-1].upper()
        middle_part = string[1:-1]
        return first_letter + middle_part + last_letter

print('capitalized string:', capitalize_first_last('hello'))

#program to swap each character in a given string with its next character using math module
import math
def swap_characters(string):
    swapped_string = ''
    for i in range(0, len(string), 2):
        if i + 1 < len(string):
            swapped_string += string[i + 1] + string[i]
        else:
            swapped_string += string[i]
    return swapped_string
print('swapped string:', swap_characters('hello'))

#program to swap each characters in a given string from lowercase to uppercase and vice versa using math module
import math
def swap_case(string):
    swapped_string = ''
    for char in string:
        if char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char.lower()
    return swapped_string
print('swapped string:', swap_case('Hello'))

#DATA FILE HANDLING IN PYTHON
#close(), read(), readline(), readlines(), write(), writelines(), seek(), tell(), flush(), readable(), writable(), 
#seekable(), isatty(), truncate(), fileno(), name, mode, closed, encoding, errors, newlines , read(n)
file = open('data.txt', 'w')
file.write('Hello, this is a sample text file.\n')
file.close()

file = open('data.txt', 'r')
content = file.read()
print('file content:', content)
file.close()

file = open('data.txt', 'a')
file.write('Appending a new line to the file.\n')
file.close()

file = open('data.txt', 'r')
lines = file.readlines()
print('file lines:', lines)
file.close()

file = open('data.txt', 'r')
line = file.readline()
print('first line:', line)
file.close()

file = open('data.txt', 'r')
content = file.read()
print('file content:', content)
file.seek(0)
content = file.read()
print('file content after seek:', content)
file.close()

#with statement for file handling
with open('data.txt', 'r') as file:
    content = file.read()
    print('file content using with statement:', content)
print('file closed after with statement:', file.closed)

#cwd = os.getcwd()
#sys.stdin, sys.stdout, sys.stderr

#program to copy content of one file to another file using file handling in python
import os
def copy_file(source_file, destination_file):
    if not os.path.exists(source_file):
        print('source file does not exist')
        return
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print('content copied from', source_file, 'to', destination_file)

copy_file('data.txt', 'destination.txt')
print('content of destination file:')
with open('destination.txt', 'r') as dest:
    print(dest.read())

#func to capitalize first and last letters of each word in a string using file handling in python
def capitalize_first_last_in_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        content = infile.read()
    words = content.split()
    capitalized_words = []
    for word in words:
        if len(word) < 2:
            capitalized_words.append(word.upper())
        else:
            first_letter = word[0].upper()
            last_letter = word[-1].upper()
            middle_part = word[1:-1]
            capitalized_words.append(first_letter + middle_part + last_letter)
    capitalized_content = ' '.join(capitalized_words)
    with open(output_file, 'w') as outfile:
        outfile.write(capitalized_content)
    print('capitalized content written to', output_file)
    capitalize_first_last_in_file('data.txt', 'capitalized_data.txt')

#program to store multiple integer values in a binary file and read them back using file handling in python
def store_integers_in_binary_file(filename, integers):
    with open(filename, 'wb') as file:
        for num in integers:
            file.write(struct.pack('i', num))

def read_integers_from_binary_file(filename):
    integers = []
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4)  # Read 4 bytes (size of an integer)
            if not data:
                break
            num = struct.unpack('i', data)[0]
            integers.append(num)
    return integers

# Example usage
integers_list = [1, 2, 3, 4, 5]
store_integers_in_binary_file('integers.bin', integers_list)
read_integers = read_integers_from_binary_file('integers.bin')
print('Read integers:', read_integers)

#program to write student data onto a csv file and read it back using file handling in python
import csv

def write_student_data_to_csv(filename, student_data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Grade'])  # Header
        writer.writerows(student_data)

def read_student_data_from_csv(filename):
    student_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            student_data.append(row)
    return student_data

# Example usage
student_records = [
    ['Alice', '20', 'A'],
    ['Bob', '22', 'B'],
    ['Charlie', '21', 'A']
]

write_student_data_to_csv('students.csv', student_records)
read_students = read_student_data_from_csv('students.csv')
print('Read student data:', read_students)


#Following is the program for performing all the operations on a table 'student' through a menu-driven program.
#Menu-driven program to demonstrate four major operations
#performed on a table through MySQL-Python connectivity 

def menu():
    c='y'
    while (c=='y'):
        print ("1. add record")
        print ("2. update record ")
        print ("3. delete record")
        print ("4. display records")
        print ("5. Exiting")
        choice = int (input ("Enter your choice: "))
        if choice == 1:
            adddata ()
        elif choice == 2:
            updatedata ()
        elif choice == 3:
            deldata()
        elif choice == 4:
            fetchdata ()
        elif choice == 5:
            break
    else:
        print ("wrong input")
c = input ("Do you want to continue or not: ")
def fetchdata():
    import mysql.connector
    try:
        db = mysql.connector.connect (host="localhost", user="root", password='', database='s1')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()
        for x in results:
            print (x)
    except:
        print ("Error: unable to fetch data")
def adddata():
    import mysql.connector
    db = mysql.connector.connect (host='localhost', user='root', password='', database='s1')
    cursor = db.cursor()
    cursor.execute("INSERT INTO student VALUES ('Ritu', 4000, 'Science', 345, 'B', '11')") 
    cursor.execute("INSERT INTO student VALUES ('Ankush', 6000, 'Commce', 445, 'A', '12')") 
    cursor.execute("INSERT INTO student VALUES ('Pihu', 3566, 'Humanis', 446, 'A', '11')") 
    cursor.execute("INSERT INTO student VALUES ('Tinku', 8900, 'Science', 545, 'A+', '12')")
    db.commit()
    print ("Records added")
def updatedata():
    import mysql.connector
    try:
        db = mysql.connector.connect (host="localhost", user="root", password='', database='s1')
        cursor = db.cursor()
        sql =("Update student set stipend=5000 where name='Ritu'")
        cursor.execute (sql)
        print ("Record Updated")
        db.commit()
    except Exception as e:
        print (e)
def deldata():
    import mysql.connector
    db=mysql.connector.connect (host="localhost", user="root", password='', database='s1')
    cursor = db.cursor()
    sql ="delete from student where name='Ritu'"
    cursor.execute (sql)
    print ("Record Deleted")
    db.commit()
menu ()

