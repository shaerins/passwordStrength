# length is at least 6
# contains at least one digit
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one special character

def passwordStrength(n, password):
    # determines the strength of a given password
    is_strong = 0
    chars_needed = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for i in range(0, n):
        if(password[i].isdigit() and not has_digit):
            has_digit = True
            is_strong += 1
        if(password[i].islower() and not has_lower):
            has_lower = True
            is_strong += 1
        if(password[i].isupper() and not has_upper):
            has_upper = True
            is_strong += 1
        if(password[i] in "!@#$%^&*()-+" and not has_special):
            has_special = True
            is_strong += 1

    chars_needed = max(6-n, 4-is_strong)
    if(chars_needed == 0):
        return "Strong"
    elif(chars_needed < 3):
        return "Medium"
    else:
        return "Weak"

password = input()
n = len(password)
check = passwordStrength(n, password)
print(check)
