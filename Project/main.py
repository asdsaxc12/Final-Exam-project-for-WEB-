import random
import string
c = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_password(c):
    random.shuffle(c)
    password = ''
    for _ in range(8):
        password+=random.choice(c)
    return password
print(generate_password(c))
        