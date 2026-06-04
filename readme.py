

# MINI PROJECT USING PYTHON

import random

target = random.randint(0,100)

target=55
while True:
     choice= (input("Guess the target or Quit(Q):"))
     if(choice=="Q"):
          break
     
     choice = int(choice)
     if(choice==target):
          print("Success:Correct guess!")
          
          break
         
     elif(choice< target):
          print("Your number is less than target")
     else:
          print("Your number is greater than target")
     

print("Game over")

# For Password (Suggested password)

import random
import string
pass_len=12
char = string.ascii_letters+string.digits+string.punctuation

#  list comprehension [function for i in range (n)]

password="/".join([random.choice(char) for i in range (pass_len)])

# password =""
# for i in range (pass_len):
#     password+= random.choice(char)

print("your random password is:",password)
