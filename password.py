

import random

while True:

    small=input("abcdefghijklmnopqrstuvwxyz")
    capital=input("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    number=int(input("0123456789"))
    symbol=input("!@#$%^&*()_+=-?/.,<>:}{[]}")

    password= input("enter password: ")
    if len(password)=="18":
        print("correct")
        for i in range ("18"):
            password_rule=random.choices(small+capital+number+symbol)


