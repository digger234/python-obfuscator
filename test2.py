import random
import string
import time
import hashlib
import base64
import json

class UserManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}
        
    def create_user(self, username, password, email):
        if username in self.users:
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = {
            'password': hashed_password,
            'email': email,
            'created_at': time.time(),
            'is_active': True
        }
        return True
    
    def authenticate(self, username, password):
        if username not in self.users:
            return None
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.users[username]['password'] == hashed_password:
            session_token = self.generate_session_token()
            self.sessions[session_token] = username
            return session_token
        return None
    
    def generate_session_token(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    
    def get_user_info(self, session_token):
        if session_token not in self.sessions:
            return None
        username = self.sessions[session_token]
        return self.users.get(username)
    
    def update_user(self, session_token, **kwargs):
        if session_token not in self.sessions:
            return False
        username = self.sessions[session_token]
        for key, value in kwargs.items():
            if key in self.users[username]:
                self.users[username][key] = value
        return True
    
    def delete_user(self, session_token):
        if session_token not in self.sessions:
            return False
        username = self.sessions[session_token]
        del self.users[username]
        del self.sessions[session_token]
        return True

class Calculator:
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Error: Division by zero")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []
    
    def store_memory(self, value):
        self.memory = value
    
    def recall_memory(self):
        return self.memory
    
    def clear_memory(self):
        self.memory = 0

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add_data(self, item):
        self.data.append(item)
    
    def remove_data(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None
    
    def sort_data(self, reverse=False):
        self.data.sort(reverse=reverse)
    
    def filter_data(self, condition):
        return [item for item in self.data if condition(item)]
    
    def map_data(self, func):
        return [func(item) for item in self.data]
    
    def get_statistics(self):
        if not self.data:
            return None
        numeric_data = [item for item in self.data if isinstance(item, (int, float))]
        if not numeric_data:
            return None
        return {
            'count': len(numeric_data),
            'sum': sum(numeric_data),
            'average': sum(numeric_data) / len(numeric_data),
            'min': min(numeric_data),
            'max': max(numeric_data)
        }

class StringManipulator:
    def __init__(self, text):
        self.text = text
    
    def to_uppercase(self):
        return self.text.upper()
    
    def to_lowercase(self):
        return self.text.lower()
    
    def reverse(self):
        return self.text[::-1]
    
    def count_words(self):
        return len(self.text.split())
    
    def count_characters(self):
        return len(self.text)
    
    def remove_whitespace(self):
        return ''.join(self.text.split())
    
    def capitalize_words(self):
        return ' '.join(word.capitalize() for word in self.text.split())
    
    def encode_base64(self):
        return base64.b64encode(self.text.encode()).decode()
    
    def decode_base64(self):
        try:
            return base64.b64decode(self.text.encode()).decode()
        except:
            return None
    
    def hash_md5(self):
        return hashlib.md5(self.text.encode()).hexdigest()
    
    def hash_sha256(self):
        return hashlib.sha256(self.text.encode()).hexdigest()

class FileManager:
    def __init__(self):
        self.files = {}
    
    def create_file(self, filename, content=""):
        if filename in self.files:
            return False
        self.files[filename] = {
            'content': content,
            'created_at': time.time(),
            'modified_at': time.time(),
            'size': len(content)
        }
        return True
    
    def read_file(self, filename):
        if filename not in self.files:
            return None
        return self.files[filename]['content']
    
    def write_file(self, filename, content):
        if filename not in self.files:
            return False
        self.files[filename]['content'] = content
        self.files[filename]['modified_at'] = time.time()
        self.files[filename]['size'] = len(content)
        return True
    
    def append_file(self, filename, content):
        if filename not in self.files:
            return False
        self.files[filename]['content'] += content
        self.files[filename]['modified_at'] = time.time()
        self.files[filename]['size'] = len(self.files[filename]['content'])
        return True
    
    def delete_file(self, filename):
        if filename not in self.files:
            return False
        del self.files[filename]
        return True
    
    def list_files(self):
        return list(self.files.keys())
    
    def get_file_info(self, filename):
        return self.files.get(filename)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_email(email):
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    if '.' not in parts[1]:
        return False
    return True

def main():
    print("=== Test Script for Obfuscation Tool ===")
    print()
    
    print("Testing UserManager:")
    user_mgr = UserManager()
    user_mgr.create_user("john", "password123", "john@example.com")
    user_mgr.create_user("jane", "securepass", "jane@example.com")
    token = user_mgr.authenticate("john", "password123")
    print(f"Session token: {token[:10]}...")
    print(f"User info: {user_mgr.get_user_info(token)['email']}")
    print()
    
    print("Testing Calculator:")
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"7 * 6 = {calc.multiply(7, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"History: {calc.get_history()}")
    print()
    
    print("Testing DataProcessor:")
    processor = DataProcessor()
    for i in range(10):
        processor.add_data(random.randint(1, 100))
    processor.sort_data()
    stats = processor.get_statistics()
    print(f"Statistics: {stats}")
    print()
    
    print("Testing StringManipulator:")
    text = StringManipulator("Hello World from Obfuscation Tool")
    print(f"Uppercase: {text.to_uppercase()}")
    print(f"Reversed: {text.reverse()}")
    print(f"Word count: {text.count_words()}")
    print(f"SHA256: {text.hash_sha256()[:16]}...")
    print()
    
    print("Testing Mathematical Functions:")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Primes up to 30: {get_primes(30)}")
    print(f"Factorial(5): {factorial(5)}")
    print()
    
    print("Testing Sorting and Searching:")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test_arr}")
    sorted_arr = bubble_sort(test_arr.copy())
    print(f"Sorted: {sorted_arr}")
    print(f"Binary search for 22: Index {binary_search(sorted_arr, 22)}")
    print()
    
    print("Testing Utilities:")
    print(f"Random password: {generate_random_password(12)}")
    print(f"Email validation for 'test@example.com': {validate_email('test@example.com')}")
    print(f"Email validation for 'invalid.email': {validate_email('invalid.email')}")
    print()
    
    print("=== All Tests Completed Successfully ===")

if __name__ == "__main__":
    main()
