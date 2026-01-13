import math as m
from memory_profiler import memory_usage
import timeit

# Return all prime numbers upto N.
# Source - https://stackoverflow.com/a/35391307
# Posted by cafebabe1991
# Retrieved 2026-01-09, License - CC BY-SA 3.0

# def fun(number):
#  #Not counting 1 in the sequence as its not prime
#  for num in range(2, number + 1) :
#     isPrime = True
#     for i in range(2, num) :
#          if (num % i) == 0 :
#         isPrime = False  
#             break
#     if isPrime:
#         print num
# fun(10) 

# prime_list = []
# while True:
#     prime_rng = input("Enter the N: ")
#     try:
#         rng = int(prime_rng)
#         for i in range(2, rng + 1):
#             is_prime = True
#             for j in range(2, i):
#                 if (i % j) == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 prime_list.append(i)
#         print(prime_list)            
#     except ValueError as e:
#         print("Error!")

     

# def gen_prime_trial(n_primes):
#     """Generate prime numbers using the Naive method."""
#     if n_primes == 0:
#         return []
    
#     primes = [2]
#     num = 3
#     while len(primes) < n_primes:
#         is_prime = True
#         for p in primes:
#             if p * p > num:
#                 break
#             if num % p == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#         num += 2
#     return primes

# while True:
#     try: 
#         n = int(input("Enter a number N or  '0' to exit: "))
#         if n < 1:
#             print("Exiting..")
#             break

#     except ValueError:
#         print("Error!")
#         continue
#     display = gen_prime_trial(n) 
#     print(display)           

def prime_sieve(n_primes):
    """Sieve of Eratosthenes for prime number generator.
    Estimate upper boundary using n-th prime approximation:
    p_n = n * log(n) + n * log(log(n))"""
    n = n_primes
    if n < 6:
        upper = 15
    else:
        upper = int(n * (m.log(n) + m.log(m.log(n)))) + 1

    sieve = [True] * (upper + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(upper ** 0.5) + 1):
        if sieve[i]:
            for  j in range(i*i, upper+1, i):
                sieve[j] = False
    primes = [i for i, val in enumerate(sieve) if val]
    return primes[:n_primes]    
    
while True:
    try: 
        n = int(input("Enter a number N or  '0' to exit: "))
        if n < 1:
            print("Exiting..")
            break

    except ValueError:
        print("Error!")
        continue
    display = prime_sieve(n)
    time_info = timeit.timeit(lambda: prime_sieve(n), number=10)
    print(f"Time taken for 10 runs (in seconds): {time_info}")
    memory_usage_info = memory_usage(-1, interval=0.1, timeout=1)
    print(f"Memory usage (in MiB): {memory_usage_info}") 
    print(display)        
