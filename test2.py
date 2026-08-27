import random
import string
import time
import hashlib
import base64
import json
import math
from collections import defaultdict

class UserManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def create_user(self, username, password, email):
        if username in self.users:
            return False
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = {
            'password': hashed,
            'email': email,
            'created_at': time.time(),
            'is_active': True,
            'login_count': 0
        }
        return True

    def authenticate(self, username, password):
        if username not in self.users:
            return None
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if self.users[username]['password'] == hashed:
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
            self.sessions[token] = username
            self.users[username]['login_count'] += 1
            return token
        return None

    def update_user(self, session_token, field, value):
        if session_token not in self.sessions:
            return False
        username = self.sessions[session_token]
        if field in self.users[username]:
            self.users[username][field] = value
            return True
        return False

    def delete_user(self, session_token):
        if session_token not in self.sessions:
            return False
        username = self.sessions[session_token]
        del self.users[username]
        del self.sessions[session_token]
        return True

    def has_role(self, username, role):
        if username in self.users:
            return self.users[username].get('role', 'user') == role
        return False

    def get_active_users(self):
        return [u for u, info in self.users.items() if info['is_active']]

    def search_users(self, query):
        return [u for u, info in self.users.items() if query.lower() in info['email'].lower()]

class Calculator:
    def __init__(self):
        self.history = []
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self.history.append("{} + {} = {}".format(a, b, result))
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append("{} - {} = {}".format(a, b, result))
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append("{} * {} = {}".format(a, b, result))
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append("{} / {} = Error".format(a, b))
            return None
        result = a / b
        self.history.append("{} / {} = {}".format(a, b, result))
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self.history.append("{} ^ {} = {}".format(base, exponent, result))
        return result

    def mod(self, a, b):
        if b == 0:
            return None
        result = a % b
        self.history.append("{} % {} = {}".format(a, b, result))
        return result

    def get_history(self):
        return self.history

    def store_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

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

    def reduce_data(self, func, init):
        result = init
        for item in self.data:
            result = func(result, item)
        return result

    def chunk_data(self, size):
        chunks = []
        for i in range(0, len(self.data), size):
            chunks.append(self.data[i:i + size])
        return chunks

    def unique_data(self):
        seen = set()
        result = []
        for item in self.data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def get_statistics(self):
        if not self.data:
            return None
        numeric = [item for item in self.data if isinstance(item, (int, float))]
        if not numeric:
            return None
        return {
            'count': len(numeric),
            'sum': sum(numeric),
            'average': sum(numeric) / len(numeric),
            'min': min(numeric),
            'max': max(numeric)
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

    def hash_md5(self):
        return hashlib.md5(self.text.encode()).hexdigest()

    def hash_sha256(self):
        return hashlib.sha256(self.text.encode()).hexdigest()

    def caesar_cipher(self, shift):
        result = []
        for char in self.text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)

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

    def search_files(self, keyword):
        results = []
        for name, info in self.files.items():
            if keyword in info['content']:
                results.append(name)
        return results

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        visited = set([start])
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            order.append(node)
            for nb in self.adj[node]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return order

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        for nb in self.adj[start]:
            if nb not in visited:
                result.extend(self.dfs(nb, visited))
        return result

    def shortest_path(self, start, end):
        if start == end:
            return [start]
        visited = {start}
        queue = [(start, [start])]
        while queue:
            node, path = queue.pop(0)
            for nb in self.adj[node]:
                if nb == end:
                    return path + [nb]
                if nb not in visited:
                    visited.add(nb)
                    queue.append((nb, path + [nb]))
        return None

    def connected_components(self):
        visited = set()
        components = []
        for vertex in self.adj:
            if vertex not in visited:
                component = []
                stack = [vertex]
                while stack:
                    node = stack.pop()
                    if node in visited:
                        continue
                    visited.add(node)
                    component.append(node)
                    for nb in self.adj[node]:
                        if nb not in visited:
                            stack.append(nb)
                components.append(sorted(component))
        return sorted(components)

class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def autocomplete(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._collect(node, prefix, results)
        return results

    def _collect(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._collect(child, prefix + ch, results)

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
        self.hits = 0
        self.misses = 0

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            self.hits += 1
            return self.cache[key]
        self.misses += 1
        return None

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        self.cache[key] = value
        self.order.append(key)
        if len(self.cache) > self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]

    def stats(self):
        total = self.hits + self.misses
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': self.hits / total if total > 0 else 0,
            'size': len(self.cache)
        }

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, state):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = state

    def count_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r = row + dr
                c = col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r][c]
        return count

    def step(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if neighbors in (2, 3):
                        new_grid[r][c] = 1
                else:
                    if neighbors == 3:
                        new_grid[r][c] = 1
        self.grid = new_grid

    def get_population(self):
        return sum(sum(row) for row in self.grid)

    def run(self, steps):
        populations = []
        for _ in range(steps):
            populations.append(self.get_population())
            self.step()
        return populations

class SortAlgorithms:
    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = SortAlgorithms.merge_sort(arr[:mid])
        right = SortAlgorithms.merge_sort(arr[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortAlgorithms.quick_sort(left) + middle + SortAlgorithms.quick_sort(right)

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, name, func):
        self.stages.append((name, func))
        return self

    def execute(self, data):
        current = data
        for name, func in self.stages:
            current = func(current)
        return current

class EncodingSuite:
    @staticmethod
    def caesar(text, shift):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def vigenere_encrypt(text, key):
        result = []
        key_idx = 0
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_idx % len(key)].lower()) - ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
                key_idx += 1
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def vigenere_decrypt(text, key):
        result = []
        key_idx = 0
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_idx % len(key)].lower()) - ord('a')
                result.append(chr((ord(char) - base - shift) % 26 + base))
                key_idx += 1
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def xor_cipher(data, key):
        key_bytes = key.encode() if isinstance(key, str) else key
        data_bytes = data.encode() if isinstance(data, str) else data
        return bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes))

    @staticmethod
    def run_length_encode(text):
        if not text:
            return ''
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(text[i - 1])
                if count > 1:
                    result.append(str(count))
                count = 1
        result.append(text[-1])
        if count > 1:
            result.append(str(count))
        return ''.join(result)

    @staticmethod
    def run_length_decode(encoded):
        result = []
        i = 0
        while i < len(encoded):
            char = encoded[i]
            i += 1
            num_str = ''
            while i < len(encoded) and encoded[i].isdigit():
                num_str += encoded[i]
                i += 1
            count = int(num_str) if num_str else 1
            result.append(char * count)
        return ''.join(result)

class TreeBuilder:
    def build_bst(self, values):
        root = None
        for val in values:
            root = self._insert(root, val)
        return root

    def _insert(self, node, val):
        if node is None:
            return {'val': val, 'left': None, 'right': None}
        if val < node['val']:
            node['left'] = self._insert(node['left'], val)
        elif val > node['val']:
            node['right'] = self._insert(node['right'], val)
        return node

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node['left'], result)
            result.append(node['val'])
            self.inorder(node['right'], result)
        return result

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node['left']), self.height(node['right']))

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
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
    return ''.join(random.choice(characters) for _ in range(length))

def validate_email(email):
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    if '.' not in parts[1]:
        return False
    return True

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    return result

def spiral_order(matrix):
    result = []
    if not matrix:
        return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

def main():
    print("=== Advanced Complex Test ===")
    print()

    um = UserManager()
    um.create_user("admin", "pass123", "admin@test.com")
    um.create_user("alice", "pass456", "alice@test.com")
    um.create_user("bob", "pass789", "bob@test.com")
    token = um.authenticate("admin", "pass123")
    print("UserManager Create: {}".format(token is not None))
    print("UserManager Auth Fail: {}".format(um.authenticate("admin", "wrong") is None))
    print("UserManager Update: {}".format(um.update_user(token, "email", "new@test.com")))
    print("UserManager Active: {}".format(len(um.get_active_users())))
    print("UserManager Search: {}".format(um.search_users("alice")))
    print()

    calc = Calculator()
    print("Calc Add: {}".format(calc.add(5, 3)))
    print("Calc Sub: {}".format(calc.subtract(10, 4)))
    print("Calc Mul: {}".format(calc.multiply(7, 6)))
    print("Calc Div: {}".format(calc.divide(15, 3)))
    print("Calc Div Zero: {}".format(calc.divide(10, 0)))
    print("Calc Power: {}".format(calc.power(2, 8)))
    print("Calc Mod: {}".format(calc.mod(17, 5)))
    print("Calc History: {}".format(len(calc.get_history())))
    print()

    dp = DataProcessor()
    for i in range(10):
        dp.add_data(random.randint(1, 100))
    dp.sort_data()
    stats = dp.get_statistics()
    print("DataProcessor Stats: {}".format(stats is not None))
    filtered = dp.filter_data(lambda x: x > 50)
    mapped = dp.map_data(lambda x: x * 2)
    reduced = dp.reduce_data(lambda a, b: a + b, 0)
    print("DataProcessor Filter: {}".format(len(filtered)))
    print("DataProcessor Map: {}".format(len(mapped)))
    print("DataProcessor Reduce: {}".format(reduced > 0))
    chunks = dp.chunk_data(3)
    print("DataProcessor Chunk: {}".format(len(chunks)))
    unique = dp.unique_data()
    print("DataProcessor Unique: {}".format(len(unique)))
    print()

    sm = StringManipulator("Hello World from Obfuscation Tool")
    print("String Upper: {}".format(sm.to_uppercase()))
    print("String Reverse: {}".format(sm.reverse()))
    print("String Words: {}".format(sm.count_words()))
    print("String Base64: {}".format(len(sm.encode_base64()) > 20))
    print("String SHA256: {}".format(len(sm.hash_sha256()) == 64))
    cipher = StringManipulator("AttackAtDawn")
    print("Caesar Cipher: {}".format(cipher.caesar_cipher(3) == "DwwdfnDwGdzq"))
    print()

    fm = FileManager()
    fm.create_file("test.txt", "Hello World")
    fm.create_file("data.txt", "Some data here")
    print("File Create: {}".format("test.txt" in fm.list_files()))
    print("File Read: {}".format(fm.read_file("test.txt") == "Hello World"))
    print("File Write: {}".format(fm.write_file("test.txt", "Updated")))
    print("File Append: {}".format(fm.append_file("test.txt", " content")))
    print("File Search: {}".format(fm.search_files("data")))
    print("File Delete: {}".format(fm.delete_file("test.txt")))
    print()

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    print("Graph BFS: {}".format(len(g.bfs(0)) == 4))
    print("Graph DFS: {}".format(len(g.dfs(0)) == 4))
    print("Graph Shortest: {}".format(g.shortest_path(0, 3) is not None))
    print("Graph Components: {}".format(len(g.connected_components()) == 2))
    print()

    trie = Trie()
    for w in ['hello', 'help', 'hero', 'heap', 'heat', 'home', 'horse']:
        trie.insert(w)
    print("Trie Search: {}".format(trie.search('hello')))
    print("Trie NoSearch: {}".format(not trie.search('hell')))
    print("Trie Prefix: {}".format(trie.starts_with('he')))
    print("Trie Auto: {}".format(len(trie.autocomplete('he')) == 5))
    print()

    lru = LRUCache(3)
    lru.put('a', 1)
    lru.put('b', 2)
    lru.put('c', 3)
    lru.get('a')
    lru.put('d', 4)
    print("LRU Get: {}".format(lru.get('a') == 1))
    print("LRU Evict: {}".format(lru.get('b') is None))
    print("LRU Stats: {}".format(lru.stats()['hit_rate'] > 0))
    print()

    gol = GameOfLife(10, 10)
    gol.set_cell(1, 2, 1)
    gol.set_cell(2, 2, 1)
    gol.set_cell(3, 2, 1)
    populations = gol.run(5)
    print("GameOfLife: {}".format(len(populations) == 5 and populations[0] == 3))
    print()

    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("Merge Sort: {}".format(SortAlgorithms.merge_sort(arr1.copy()) == sorted(arr1)))
    print("Quick Sort: {}".format(SortAlgorithms.quick_sort(arr1.copy()) == sorted(arr1)))
    print("Insertion Sort: {}".format(SortAlgorithms.insertion_sort(arr1.copy()) == sorted(arr1)))
    print()

    ppl = Pipeline()
    ppl.add_stage('double', lambda x: [i * 2 for i in x])
    ppl.add_stage('filter', lambda x: [i for i in x if i > 10])
    ppl.add_stage('sum', lambda x: sum(x))
    print("Pipeline: {}".format(ppl.execute([1, 2, 3, 4, 5, 6, 7]) == 26))
    print()

    enc = EncodingSuite()
    encoded = enc.caesar('Hello', 3)
    print("Caesar Enc: {}".format(encoded == 'Khoor'))
    print("Caesar Dec: {}".format(enc.caesar(encoded, -3) == 'Hello'))
    vig = enc.vigenere_encrypt('Attack', 'LEMON')
    print("Vigenere: {}".format(enc.vigenere_decrypt(vig, 'LEMON') == 'Attack'))
    rle = enc.run_length_encode('aaabbbcc')
    print("RLE Enc: {}".format(rle == 'a3b3c2'))
    print("RLE Dec: {}".format(enc.run_length_decode(rle) == 'aaabbbcc'))
    xor = enc.xor_cipher('test', 'key')
    print("XOR: {}".format(enc.xor_cipher(xor, 'key') == b'test'))
    print()

    tb = TreeBuilder()
    tree = tb.build_bst([5, 3, 7, 1, 4, 6, 8])
    print("BST Inorder: {}".format(tb.inorder(tree) == [1, 3, 4, 5, 6, 7, 8]))
    print("BST Height: {}".format(tb.height(tree) == 3))
    print()

    print("Fibonacci: {}".format(fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))
    print("Primes: {}".format(get_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]))
    print("Factorial: {}".format(factorial(6) == 720))
    print()

    sorted_arr = bubble_sort([64, 34, 25, 12, 22, 11, 90])
    print("Bubble Sort: {}".format(sorted_arr == sorted([64, 34, 25, 12, 22, 11, 90])))
    idx = binary_search(sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 7)
    print("Binary Search: {}".format(idx == 6))
    print()

    print("Email Valid: {}".format(validate_email('test@example.com')))
    print("Email Invalid: {}".format(not validate_email('invalid.email')))
    wf = word_frequency("the cat sat on the mat the cat")
    print("Word Freq: {}".format(wf.get('the', 0) == 3 and wf.get('cat', 0) == 2))
    print()

    flat = flatten([1, [2, 3], [4, [5, 6]], 7])
    print("Flatten: {}".format(flat == [1, 2, 3, 4, 5, 6, 7]))
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Rotate Matrix: {}".format(rotate_matrix(mat) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]))
    print("Spiral: {}".format(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]))
    print()

    print("Lambda Map: {}".format(list(map(lambda x: x**2, [1, 2, 3])) == [1, 4, 9]))
    print("Lambda Filter: {}".format(list(filter(lambda x: x > 3, [1, 2, 3, 4, 5])) == [4, 5]))
    print("Zip: {}".format(list(zip(['a', 'b'], [1, 2])) == [('a', 1), ('b', 2)]))
    print()

    inv_d = {v: k for k, v in {'x': 1, 'y': 2}.items()}
    print("Dict Comp: {}".format(inv_d == {1: 'x', 2: 'y'}))
    sq = [x**2 for x in range(5)]
    print("List Comp: {}".format(sq == [0, 1, 4, 9, 16]))
    print()

    dd = defaultdict(int)
    for ch in 'mississippi':
        dd[ch] += 1
    print("DefaultDict: {}".format(dd['s'] == 4 and dd['p'] == 2))
    print()

    print("=== All Tests Completed Successfully ===")

if __name__ == "__main__":
    main()
