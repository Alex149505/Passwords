def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)  
    

def has_upper_letters(password):
    return any(char.isupper() for char in password) 


def has_lower_letters(password):
    return any(char.islower() for char in password) 


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def count_score(password):
    functions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    score = 0
    for function in functions:
        if function(password):
            score += 2
    print(f'надежность пароля {score}')        
    return score  


def main():
    password = input('input password: ')
    count_score(password)  
    

if __name__ == "__main__":
    main()







