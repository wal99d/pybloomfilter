import hashlib, math

class BloomFilter:
  def __init__(self, capacity, error_rate):
    self.capacity = capacity
    self.error_rate = error_rate
    self.num_bits = int(-(capacity * math.log(error_rate)) / (math.log(2) ** 2)) # Number of bits needed
    self.num_hashes = int((self.num_bits / capacity) * math.log(2)) # Number of hash functions needed
    self.bits = bytearray(self.num_bits)

  def add(self, key):
    for i in range(self.num_hashes):
      h = hashlib.sha256(str(key).encode('utf-8') + str(i).encode('utf-8')).hexdigest() # Using sha256 hash function
      bit_index = int(h, 16) % self.num_bits
      self.bits[bit_index] = 1

  def contains(self, key):
    for i in range(self.num_hashes):
      h = hashlib.sha256(str(key).encode('utf-8') + str(i).encode('utf-8')).hexdigest() # Using sha256 hash function
      bit_index = int(h, 16) % self.num_bits
      if not self.bits[bit_index]:
        return False
    return True

  def remove(self, key):
    for i in range(self.num_hashes):
      h = hashlib.sha256(str(key).encode('utf-8') + str(i).encode('utf-8')).hexdigest() # Using sha256 hash function
      bit_index = int(h, 16) % self.num_bits
      if self.bits[bit_index]:
        self.bits[bit_index] = 0
        return True
    return False # Key not found

# Create a Bloom Filter with capacity 100000 and error rate 0.001
bf = BloomFilter(100000, 0.001)

# Add some keys to the Bloom Filter
bf.add('apple')
bf.add('banana')
bf.add('orange')

# Check if a key is present in the Bloom Filter
print(bf.contains('apple')) # True
print(bf.contains('grapefruit')) # False

# Remove a key from the Bloom Filter
print(bf.remove('banana')) # True
print(bf.contains('banana')) # False
