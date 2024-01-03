import random
import string
print("$#  Password Generetor $#")


alphabet = string.ascii_letters  #every alphabet character
nums = string.digits  # 0 to 10
punctuation = string.punctuation
main = alphabet + nums + punctuation

amount = int(input("Please enter the number of passwords you need?: "))
lenght = int(input("please enter the desired lenght of each password: "))


print(f"\n your {amount} generated passwords are:")
for i in range(amount):
     password = ""
     for y in range(lenght):
          password += random.choice(main)
     print(password) 

print("\n ### Thank You for using our generator ###")