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
def get_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

start_range = 0
end_range = 10000
prime_numbers_list = get_prime_numbers(start_range, end_range)
print(f"Список простых чисел в диапазоне от {start_range} до {end_range}:")
print(prime_numbers_list)