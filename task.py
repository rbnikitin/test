import random

def checksum(l):
  chsum = 0
  for i in l:
    chsum = (chsum + i) * 113
  chsum = chsum % 10000007  
  return chsum


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 1
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


numbers = generate_primes(1000)
random.Random(100).shuffle(numbers)
#print(numbers)
print(checksum(numbers))
