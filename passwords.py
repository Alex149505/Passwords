PASSWORD = input('input password: ')


def is_very_long(PASSWORD):
    return len(PASSWORD) >= 12


def has_digit(PASSWORD):
    return any(char.isdigit() for char in PASSWORD)


def has_letters(PASSWORD):
    return any(char.isalpha() for char in PASSWORD)  
    

def has_upper_letters(PASSWORD):
    return any(char.isupper() for char in PASSWORD) 


def has_lower_letters(PASSWORD):
    return any(char.islower() for char in PASSWORD) 


def has_symbols(PASSWORD):
    return any(not char.isalnum() for char in PASSWORD)


def count_score(PASSWORD):
    functions = [is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    score = 0
    for function in functions:
        if function(PASSWORD):
            score += 2
    print(f'надежность пароля {score}')        
    return score  


def main():
    count_score(PASSWORD)  


if __name__ == "__main__":
    main()







