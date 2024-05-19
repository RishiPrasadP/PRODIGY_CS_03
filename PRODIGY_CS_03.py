import re

def check_length(password):
    if len(password) >= 8:
        return True
    return False

def check_uppercase(password):
    if re.search(r"[A-Z]", password):
        return True
    return False

def check_lowercase(password):
    if re.search(r"[a-z]", password):
        return True
    return False

def check_number(password):
    if re.search(r"\d", password):
        return True
    return False

def check_special_char(password):
    if re.search(r"[!@#$%^&*()-_=+{};:'\",<.>/?\|\\]", password):
        return True
    return False

def assess_password_strength(password):
    criteria_met = 0

    if check_length(password):
        criteria_met += 1
    if check_uppercase(password):
        criteria_met += 1
    if check_lowercase(password):
        criteria_met += 1
    if check_number(password):
        criteria_met += 1
    if check_special_char(password):
        criteria_met += 1

    if criteria_met == 5:
        return "Very Strong"
    elif criteria_met == 4:
        return "Strong"
    elif criteria_met == 3:
        return "Moderate"
    elif criteria_met == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter the password to assess its strength: ")
    strength = assess_password_strength(password)
    print("Password Strength:", strength)

if __name__ == "__main__":
    main()
