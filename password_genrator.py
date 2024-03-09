import random
latters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=[0,1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
n_latters=int(input("How many latters would you like in your password:"))
n_symbols=int(input("How many symbols would you like:"))
n_numbers=int(input("How many numbers would you like:"))
password_list=[]
for i in range(1,n_latters+1):
  char=random.choice(latters)
  password_list+=char
for i in range(1,n_symbols+1):
  char=random.choice(symbols)
  password_list+=char
for i in range(1,n_numbers+1):
  char=(random.choice(numbers))
  char=str(char)
  password_list+=char
random.shuffle(password_list)
# print(password_list)
password=""
for char in password_list:
  password+=char
print("Your password is")
print(password)
