# length is at least 6
# contains at least one digit
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one special character

def minimumNumber(n, password):
    # determines the strength of a given password
    password = list(password)
    isStrong = 0
    charsNeeded = 0
    hasLower = False
    hasUpper = False
    hasDigit = False
    hasSpecial = False
    for i in range(0, n):
        if(password[i].isdigit() and not hasDigit):
            hasDigit = True
            isStrong += 1
        if(password[i].islower() and not hasLower):
            hasLower = True
            isStrong = 1
        if(password[i].isupper() and not hasUpper):
            hasUpper = True
            isStrong += 1
        if(password[i] in "!@#$%^&*()-+" and not hasSpecial):
            hasSpecial = True
            isStrong += 1
            
    charsNeeded = max(6-n, 4-isStrong)
    if(charsNeeded == 0):
        print("Strong")
    elif(charsNeeded < 3):
        print("Medium")
    else:
        print("Weak")

password = input()
n = len(password)
check = minimumNumber(n, password)
print(check)
