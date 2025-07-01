import threading

def is_prime(n):
    """Tub son ekanligini tekshiradi"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    """Berilgan oraliqdagi tub sonlarni aniqlaydi va ro'yxatga qo'shadi"""
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)

def divide_range(start, end, num_threads):
    """Umumiy oraliqni num_threads ta bo‘lakka ajratadi"""
    step = (end - start + 1) // num_threads
    ranges = []
    for i in range(num_threads):
        range_start = start + i * step
        range_end = start + (i + 1) * step - 1
        if i == num_threads - 1:
            range_end = end  # oxirgi bo‘lak to‘liq qamrab oladi
        ranges.append((range_start, range_end))
    return ranges

def threaded_prime_checker(start, end, num_threads):
    threads = []
    primes = []

    # Har bir thread uchun alohida natija ro‘yxati
    results = [[] for _ in range(num_threads)]

    ranges = divide_range(start, end, num_threads)

    for i in range(num_threads):
        t = threading.Thread(target=check_primes, args=(ranges[i][0], ranges[i][1], results[i]))
        threads.append(t)
        t.start()

    # Barcha threadlar tugashini kutamiz
    for t in threads:
        t.join()

    # Natijalarni birlashtiramiz
    for res in results:
        primes.extend(res)

    # Saralaymiz
    primes.sort()
    return primes

# === Ishga tushirish ===
if __name__ == "__main__":
    start = 1
    end = 1000
    num_threads = 4  # Nechta oqimda bo‘lishni belgilaymiz

    print(f"Checking prime numbers from {start} to {end} using {num_threads} threads...")
    primes = threaded_prime_checker(start, end, num_threads)

    print(f"\nFound {len(primes)} prime numbers:")
    print(primes)


import threading
from collections import Counter
import time

def read_file_lines(file_path):
    """Fayldagi barcha qatorlarni o'qiydi"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def count_words(lines, result_list, index):
    """Berilgan qatorlar ichidagi so'zlar sonini hisoblaydi"""
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_list[index] = word_count

def threaded_word_counter(file_path, num_threads=4):
    lines = read_file_lines(file_path)
    total_lines = len(lines)
    step = total_lines // num_threads

    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * step
        end = total_lines if i == num_threads - 1 else (i + 1) * step
        t = threading.Thread(target=count_words, args=(lines[start:end], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Barcha natijalarni birlashtirish
    final_count = Counter()
    for partial_count in results:
        final_count.update(partial_count)

    return final_count

# === Test uchun ===
if __name__ == "__main__":
    import os

    # Fayl yaratamiz (agar mavjud bo'lmasa)
    test_file = "sample_text.txt"
    if not os.path.exists(test_file):
        with open(test_file, 'w', encoding='utf-8') as f:
            for _ in range(10000):  # Katta fayl yaratamiz
                f.write("Threading in Python is powerful and threading can be tricky.\n")

    start_time = time.time()
    word_counts = threaded_word_counter(test_file, num_threads=4)
    end_time = time.time()

    print("\nTop 10 most frequent words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

    print(f"\nTime taken: {end_time - start_time:.2f} seconds")
