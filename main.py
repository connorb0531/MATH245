import random
from math import gcd

# Check if a number is prime
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime within a range
def generate_prime(start=100, end=300):
    primes = [x for x in range(start, end) if is_prime(x)]
    return random.choice(primes)

# Euler’s Phi Function
def compute_phi(p, q):
    return (p - 1) * (q - 1)

# Choose e such that gcd(e, phi) = 1
def choose_e(phi):
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    return e

# Modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return (1, 0)
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (x, y)

    x, _ = extended_gcd(e, phi)
    return x % phi

# Encrypt message
def encrypt(message, e, n):
    return pow(message, e, n)

# Decrypt message
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# RSA Demo
# Generate two distinct primes
p = generate_prime()
q = generate_prime()
while p == q:
    q = generate_prime()

n = p * q
phi_n = compute_phi(p, q)
e = choose_e(phi_n)
d = mod_inverse(e, phi_n)

# Display information
print(f"Prime p: {p}, Prime q: {q}")
print(f"n = p * q = {n}")
print(f"phi(n) = (p-1)(q-1) = {phi_n}")
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")

# Test encryption and decryption
message = 42
ciphertext = encrypt(message, e, n)
decrypted = decrypt(ciphertext, d, n)

print(f"\nOriginal Message: {message}")
print(f"Encrypted Message: {ciphertext}")
print(f"Decrypted Message: {decrypted}")
