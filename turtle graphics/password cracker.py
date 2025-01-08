import random
from random import randint
u_pwd = input("Enter a password: ")
pwd = 'qwertyuiopasdfghjklzxcvbnm12345678901YG'
pw = ""

while pw != u_pwd:
    pw =''.join(random.choice(pwd) for i in range(len(u_pwd)))
    print("......Cracking Password...........Please wait")
print("\n\nYour Password is :", pw)




