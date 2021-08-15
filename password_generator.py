#Password Generator Project
import random

def password_maker():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter_list = [random.choice(letters) for i in range(random.randint(10, 12))]
    number_list = [random.choice(numbers) for i in range(random.randint(3, 5))]
    symbol_list = [random.choice(symbols) for i in range(random.randint(3, 5))]
    passport_list = letter_list + number_list + symbol_list
    random.shuffle(passport_list)
    return "".join(passport_list)

