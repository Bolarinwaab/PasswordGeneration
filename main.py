import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '#', '+', '!', '$', '%', '&', '(', ')', ';', '|', '=']

# Simple password generation like 4 letters, 2 numbers and 3 symbols without randomized order

num_letter = int(input("enter the number of letters in the password :  "))
num_numbers = int(input("Enter how many  numbers in the password : "))
num_symbols = int(input("Enter the number of Symbols in the password : "))

rand_letter = random.choices(letters, k =num_letter )
rand_number = random.choices(numbers, k =num_numbers)
rand_symbol = random.choices(symbols, k =num_symbols )

password = rand_letter + rand_number + rand_symbol

generated_password = ""
# for loop to loop through the list above to get password

for each_pass in password:
    generated_password = generated_password + each_pass


print(f"your password  is : {generated_password}")

password_value = rand_letter + rand_number + rand_symbol
random.shuffle(password_value)
strong_password = ""
# for loop to loop through the list above to get password

for each_value in password_value:
    strong_password = strong_password + each_value


print(f"your strong password  is : {strong_password}")