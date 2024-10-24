from encoder import encode
from decoder import decode

x=True
while x:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    print("Please enter an option: ")
    resp=int(input())
    if resp==1:
        print("Please enter your password to encode: ")
        entered=input()
        enc=encode(entered)
        print("Your password has been encoded and stored!")
    if resp==2:
        dec=decode(enc)
        print("The encoded password is",enc,", and the original password is",dec)
    if resp==3:
        x=False