import random

def generate_pass_easy(length):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    b_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    nums = '123456789'
    chars = "!@#$%^&*()"
    return ''.join(random.choice(letters) for _ in range(length))

def generate_pass_med(length):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    b_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join(random.choice(letters + b_letters) for _ in range(length))

def generate_pass_hard(length):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    b_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    nums = '123456789'
    return ''.join(random.choice(letters + b_letters + nums) for _ in range(length))

def generate_pass_extreme(length):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    b_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    nums = '123456789'
    chars = "!@#$%^&*()"
    return ''.join(random.choice(letters + b_letters + nums + chars) for _ in range(length))
    
    
    
    
    
