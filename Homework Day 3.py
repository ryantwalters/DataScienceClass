#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('You guessed correct!')


# In[8]:


import random

#We identify two variables, target_num and guess_num.
#target_num points to a random integer between the defined 1-10.
#guess_num points to 0.
#We must import the random package to provide access to the randint function.

target_num, guess_num = random.randint(1, 10), 0

#We then create a while loop that states, while target_num does not equal guess_num,
#which is defaulted to 0 but changed by user input, do nothing until it equals target_num, then print.
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('You guessed correct!')


# In[ ]:


import re

#p points to the password input from the user.
#x points to true.  That is its default definition.
p = input("Input your password : ")
x = True

#We then create a while loop, stating that as long as it meets every if condition listed, continue next.
#If it does not pass one of these tests, break the function and continue to the if statementat the end.
while x:  
    if (len(p)<6 or len(p)>12):
        break
#The condition of false
#Search the password for characters a-z.  If not, break and print x.
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")


# In[9]:


import re
p = input("Input your password : ")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        print("This password does not contain a lowercase letter!")
        break
    elif not re.search("[0-9]",p):
        print("This password does not contain a number!")
        break
    elif not re.search("[A-Z]",p):
        print("This password does not contain an uppercase letter!")
        break
    elif not re.search("[$#@]",p):
        print("This password does not contain a symbol (ex. $, #, @)")
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")


# In[2]:


number1 = int(input("Enter First Person's Age : "))
number2 = int(input("Enter Second Person's Age : "))
number3 = int(input("Enter Third Person's Age : "))

def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("The Oldest of All Three People is : ", largest_num)
    
def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    print("The Youngest Of All Three People is : ", smallest_num)
    
largest(number1, number2, number3)
smallest(number1, number2, number3)


# In[7]:


#Exercise 3
number1 = int(input("Enter First Person's Age : "))
number2 = int(input("Enter Second Person's Age : "))
number3 = int(input("Enter Third Person's Age : "))

#Here we define the function largest to determine which of the following is the largest number.
def largest(num1, num2, num3):
#If num1 is greater than both num2 and num3
    if (num1 > num2) and (num1 > num3):
#Then...
        largest_num = num1
#If num2 is greater than both num1 and num3
    elif (num2 > num1) and (num2 > num3):
#Then...
        largest_num = num2
#Otherwise we can assume that the largest number is num3 and finish our if else statement printing...
    else:
        largest_num = num3
    print("The Oldest of All Three People is : ", largest_num)
    
def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else: 
        smallest_num = num3
    print("The Youngest of All Three People is : ", smallest_num)

#Here we run the prior defined code.
largest(number1, number2, number3)
smallest(number1, number2, number3)


# In[ ]:


#number of classes held:
total = int(input("How many clases are held : "))

#number of classes attended:
attended = int(input("How many classes have you attended : "));

#percentage of classes
percentage = ((attended/total)*100);

if percentage < 75:
    print("You can not take part in the exam");
else:
    print("You are free to take part in the exam");


# In[11]:


total = int(input("How many classes are held : "))

attended = int(input("How many classes have you attended : "));

percentage = ((attended/total)*100);

if percentage < 75:
    print("You can not take part in the exam");
else:
    print("You are free to take part in the exam");


# In[ ]:


# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

N = int(input("Input a Number to see if You Are Weird or Not Weird : "))

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")


# In[6]:


N = int(input("Input a Number to see if You Are Weird or Not Weird : "))

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")


# In[30]:


b=2
def g():        # inner function
    nonlocal b  #comment
    b=3         # this will create a new local variable
    print(b)
g()
print(b)


# In[38]:


def TowerOfHanoi(n , x, destination, auxilliary): 
    if n==1: 
        print("Move disk 1 from source",x,"to destination",destination)
        return
    TowerOfHanoi(n-1, x, auxilliary, destination) 
    print("Move disk",n,"from source",x,"to destination",destination)
    TowerOfHanoi(n-1, auxilliary, destination, x)
    # Driver code 
n = 3
TowerOfHanoi(n,'A','C','B')  
# A, C, B are the name of rods


# In[42]:


def TowerOfHanoi(n , A, B, C): 
    if n==1: 
        print("1",A,B)
        return
    TowerOfHanoi(n-1, A, C, B) 
    print(n,A,B)
    TowerOfHanoi(n-1, C, B, A)
    # Driver code 
n = 3
TowerOfHanoi(n,'A','C','B')  
# A, C, B are the name of rods

