import random

def mod(n: int, u: int):
    return n%u
    
def euler(n: int):
    res = n
    i = 2
    while i**2 < n:
        while n % i == 0:
            n /= i
            res -= res / i
        i += 1
    if n > 1: 
        res -= res / n
    return int(res)

def prime_num(start: int, stop: int):
    prime_numbers=[]
    for i in range(start, stop):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

z = int(input("Input `a` value: "))
x = int(input("Input `b` value: "))
c = int(input("Input `m` value: "))

task_2 = mod(z, c)
task_3 = mod(z**x, c)
task_4 = mod(x*z**(euler(c)-1), c)
task_5 = random.choice(prime_num(z, x))

print(f'Task 2: {z} mod {c} = {task_2}')
print(f'Task 3: {z}^{x} mod {c} = {task_3}')
print(f'Task 4: {z}*{x}^(Ф({c})-1) mod {c} = {task_4}')
print(f'Task 5: Random prime number from {z} to {x} = {task_5}')
