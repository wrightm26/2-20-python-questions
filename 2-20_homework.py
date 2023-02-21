#!/usr/bin/env python
# coding: utf-8

# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

# In[1]:


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_num:
    i = i ** 3
    print(i)



# Exercise #2
# Get first prime numbers up to 100

# In[1]:


prime_numbers = []

for i in range(2,100):
    for num in prime_numbers:
        if i % num == 0:
            break
    else:
        prime_numbers.append(i)

print(prime_numbers)









# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

# In[3]:


age = input("How old are you?")
age_int = int(age)

if age_int < 18:
    print('kids')
elif age_int <= 18 or age_int < 65:
    print('adults')
else:
    print('seniors')


# In[4]:


4


# In[ ]:
