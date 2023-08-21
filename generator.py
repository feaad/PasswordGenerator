import string
import random
import re

password = []
email_list = []
mail = ''


def generator():
    '''Generates a password based on users' preferred length'''
    print("Choose a password length between 8 and 14")
    password_len = input()
    if int(password_len) < 8 or int(password_len) > 14:
        generator()
        exit()
    engine(password_len)


def engine(length: str):
    '''Creates a new password and calls the validate function'''
    new_password = ''
    special = "!@#$%&*^"
    check = ''
    try:
        character_list = string.ascii_letters + string.digits + special
        while len(password) < int(length):
            pass_char = random.choice(character_list)
            password.append(pass_char)
            new_password = "".join(password)
            check = regex_validate(new_password)
        if check == 'Valid':
            email()
            print(mail, new_password)
            to_file(mail, new_password)
        elif check == 'Invalid':
            password.clear()
            engine(length)
    except ValueError:
        print("Invalid Input")
        generator()


def regex_validate(value: str):
    '''Validates the new password using a regular expression'''
    regex = '(?=.*[A-Z])(?=.*[!@#$&%^])(?=.*[a-z])(?=.*[0-9])'
    result = re.search(regex, value)
    return 'Valid' if result else 'Invalid'


def email():
    '''Creates a random email for the user'''
    new_email = ''
    special_char = '_-.'
    validate = ''
    global mail
    email_characters = string.ascii_letters + string.digits + special_char
    email_len = random.randint(3, 15)
    while len(email_list) < email_len:
        email_char = random.choice(email_characters)
        email_list.append(email_char)
        new_email = ''.join(email_list)
        validate = validate_email(new_email)
    if validate == 'Valid':
        ext = extension()
        new_email += ext
        mail = new_email
    elif validate == 'Invalid':
        email_list.clear()
        email()


def validate_email(value: str):
    '''Check if the email is valid'''
    expression = '[a-zA-Z](?=.*[0-9])(?=.*[._-])'
    res = re.search(expression, value)
    return 'Valid' if res else 'Invalid'


def extension() -> str:
    '''Randomly adds an email extension'''
    extensions = ['@outlook.com', '@yahoo.com', '@gmail.com', '@live.com',
                  '@hotmail.com']
    return random.choice(extensions)


def to_file(emails, new_password):
    '''Print all passwords to a text file'''
    value = {}
    with open("Passwords", "w", encoding="utf-8") as my_file:
        if emails not in value:
            value[emails] = new_password
        my_file.write(str(value))


generator()