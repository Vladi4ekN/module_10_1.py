import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Вызовы функции в основном потоке
start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Время выполнения в основном потоке: {end_time - start_time:.2f} секунд")

# Функция для вызова в потоках
def thread_function(word_count, file_name):
    write_words(word_count, file_name)

# Создание потоков
threads = []
for args in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=thread_function, args=args)
    threads.append(thread)

# Запуск потоков
start_time_threads = time.time()
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time.time()
print(f"Время выполнения в потоках: {end_time_threads - start_time_threads:.2f} секунд")
