import re

def check_password(password):
    # Check for length, digit, uppercase, lowercase, and special char
    if len(password) < 8:
        return "Weak: Too short (Needs 8+ characters)"
    if not re.search("[a-z]", password):
        return "Weak: Needs lowercase letters"
    if not re.search("[A-Z]", password):
        return "Weak: Needs uppercase letters"
    if not re.search("[0-9]", password):
        return "Weak: Needs at least one number"
    if not re.search("[_@$!%*#?&]", password):
        return "Weak: Needs a special character"
    
    return "Strong: Password meets security standards"

pwd = input("Enter a password to test: ")
print(check_password(pwd))
