class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def display(self):
        print("Separate Chaining Hash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
        print()


class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + 1) % self.size
            if index == original_index:
                print("Table full!")
                return
        self.table[index] = (key, value)
    
    def display(self):
        print("Linear Probing Hash Table:")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print()


class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        i = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + i * i) % self.size
            i += 1
        self.table[index] = (key, value)
    
    def display(self):
        print("Quadratic Probing Hash Table:")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print()


class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash1(self, key):
        return hash(key) % self.size
    
    def hash2(self, key):
        return 1 + (hash(key) % (self.size - 1))
    
    def insert(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            i += 1
            index = (index + i * step) % self.size
        self.table[index] = (key, value)
    
    def display(self):
        print("Double Hashing Hash Table:")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print()


# 🔸 Kullanım:
keys = ["apple", "banana", "grape", "cherry", "orange"]

sc = SeparateChainingHashTable(5)
lp = LinearProbingHashTable(5)
qp = QuadraticProbingHashTable(5)
dh = DoubleHashingHashTable(5)

for k in keys:
    sc.insert(k, f"value_{k}")
    lp.insert(k, f"value_{k}")
    qp.insert(k, f"value_{k}")
    dh.insert(k, f"value_{k}")

sc.display()
lp.display()
qp.display()
dh.display()
