import random
import string

def generate_verification_code(length):
    verification_array = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        authentication = ''.join(random.choice(verification_array))
    return authentication

authentication_length = int(input("Enter Verficiation Code Length (Minimum Value = 6): "))
while True:
    if type(authentication_length) != int():
        authentication_length = int(input("Invalid Input! Please Enter an Integer Above or Equal to 6:"))
        
verification_code = generate_verification_code(authentication_length)
print(f"Your {authentication_length}-digit verification code is {verification_code}")
