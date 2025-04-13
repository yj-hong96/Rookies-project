
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# 테스트 코드
start = 10
end = 50
prime_numbers = find_primes(start, end)

print(f"소수 목록: {prime_numbers}")