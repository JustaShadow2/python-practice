import random
import sys

input = input("Input something")

a = random.randint(1,6)
if a == 3:
    sys.exit('hehehehaw you dont get to run the code this time. rnjesus said no. L bozo try again')

def count_upper_case(str):
    count = 0
    for i in range (len(str)):
        if str[i].isupper():
            count += 1
    return count

count = count_upper_case(input)
if count == 1:
    print('There is 1 capital letter')
if count >= 2:
    print('There are', count, 'capital letters')
if count == 0:
    print('Thats not even a valid input you absolute idiot if you pull this crap again i stg im gonna lose my shit and commit multiple illegal acts')






'''words = input("input a string")
count = 0

for char in words:
    if(char.isupper()):
        count = count + 1

print(count)''' #imagine doing things the most resource efficient way

