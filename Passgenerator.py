import random
def number():
    num_number = random.choice([5])
    number_set = {'0','1','2','3','4','5','6','7','8','9'}
    number_list = random.sample(list(number_set),num_number)
    return number_list
def symbols():
    num_symbols = random.choice([4, 5])
    symbols_set =  {    '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '|', '\\', '/', '{', '}', '[', ']', '(', ')', ':', ';', '"', "'", '`', '~', '<', '>'}
    symbols_list = random.sample(list(symbols_set), num_symbols)
    return symbols_list
def uppercase():
    num_capitals = random.choice([4,5])
    capital_set =  { 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
    capital_list = random.sample(list(capital_set),num_capitals)
    return capital_list
def lowecase():
    num_small = random.choice([4,5])
    small_set = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    small_list = random.sample(list(small_set),num_small)
    return small_list
def password():
    password_list =uppercase()+symbols()+lowecase()+number()
    main_password = random.sample(password_list,16)
    password_string = "".join(main_password)
    return password_string

if __name__ == '__main__':
    print(password())