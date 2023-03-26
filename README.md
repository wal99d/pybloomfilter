## Here's an example of how you can write a Bloom Filter in Python 3 

- In this example, we are using the sha256 hash function from the hashlib module to hash the key. We are also using a bytearray to store the bits of the Bloom Filter. The **add** function hashes the key using multiple hash functions and sets the corresponding bits in the bytearray to 1. The **contains** function checks whether a key is present in the Bloom Filter by hashing it using the same hash functions and checking whether the corresponding bits are set to 1. The **remove** function works in a similar way as the contains function but sets the corresponding bits to 0 instead.

```
Here's an example of how to use the BloomFilter class:
# Create a Bloom Filter with capacity 100000 and error rate 0.001
bf = BloomFilter(100000, 0.001)

# Add some keys to the Bloom Filter
bf.add('apple')
bf.add('banana')
bf.add('orange')

# Check if a key is present in the Bloom Filter
print(bf.contains('apple')) # True
print(bf.contains('grapefruit')) # False
```