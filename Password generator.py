import random
letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
integers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
symbols = ('#', '@', '%', '$', '!', '^', '&', '*', '(', ')')
print("Welcome to the Password Generator")
n_letters = int(input("Enter the number of letters you want:\n"))
n_integers = int(input("Enter the number of integers you want:\n"))
n_symbols = int(input("Enter the number of symbols you want:\n"))
password = ""
for i in range(1, n_letters+1):
    char = random.choice(letters)
    password = password + char
for i in range(1, n_integers+1):
    char = random.choice(integers)
    password = password + char
for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password = password + char
print("The required password is:", password)




