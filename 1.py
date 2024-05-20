import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time} секунд")
        return result
    return wrapper
@calculate_time
def get_prime_numbers():
    prime_numbers = []
    for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

prime_numbers_list = get_prime_numbers()
print("Список простых чисел от 0 до 1000:")
print(prime_numbers_list)