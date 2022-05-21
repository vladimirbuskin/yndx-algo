import sys


def is_prime(n):
  if n == 1:
    return False
  i = 2
  ar = [0]*n
  while i*i < n:
    if n % i == 0:
      return False
  return True

# find all primes
# def find_primes(n):
#   ar = list(range(n + 1))
#   ar[0] = False
#   ar[1] = False
#   i = 2
#   while i < n:
#     c = i + i
#     while c < n:
#       ar[c] = False
#       c += i
#     i += 1
#   return ar

def find_primes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = '_'
                print(numbers)
    return numbers 

print(find_primes(15))

