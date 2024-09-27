# python program to create Password Genterator
import random
import string
print("Welcome to are Random Password Generator")
def main():
   length=int(input("Enter tje length of password you want: "))
   lowerD=string.ascii_lowercase
   upperD=string.ascii_uppercase
   digitD=string.digits
   symnolsD=string.punctuation
   combine=lowerD+upperD+digitD+symnolsD
   x=random.sample(combine,length)
   password="".join(x)
   print(password)
   main()
main()   










