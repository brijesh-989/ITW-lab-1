import random
import string
def randompassword(strLen=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(strLen))

print("Generating Random String password with letters, digits and special characters ")
print("First Random String:",randompassword())
print("Second Random String:",randompassword())
print("Third Random String:",randompassword())
