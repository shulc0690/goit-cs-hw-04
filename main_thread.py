import threading
import os
import time
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def search_keywords_in_file(file_path, keywords, result):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for keyword in keywords:
                count = content.count(keyword)
                if count > 0:
                    result.setdefault(keyword, []).append((file_path, count))
                    logging.info(
                        f"Keyword '{keyword}' found {count} times in {file_path}"
                    )
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")


def thread_worker(files, keywords, result):
    for file in files:
        search_keywords_in_file(file, keywords, result)


def multithreading_search(files, keywords):
    num_threads = min(10, len(files))
    threads = []
    results = [{} for _ in range(num_threads)]

    # Розподіл читання файлів на потоки
    for i in range(num_threads):
        thread_files = files[i::num_threads]
        t = threading.Thread(
            target=thread_worker, args=(thread_files, keywords, results[i])
        )
        threads.append(t)
        t.start()
        logging.info(f"Thread {t.name} started")

    for t in threads:
        t.join()
        logging.info(f"Thread {t.name} finished")

    # Об'єднення результатів пошуку
    final_result = {}
    for result in results:
        for keyword, occurrences in result.items():
            if keyword in final_result:
                final_result[keyword].extend(occurrences)
            else:
                final_result[keyword] = occurrences

    return final_result


def get_files_from_directory(directory):
    return [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".txt")
    ]


if __name__ == "__main__":
    directory = "random_texts"  # Директорія з файлами
    files = get_files_from_directory(directory)
    keywords = ["OK", "Coca-Cola", "CORONA"]  # Слова для пошуку
    print(f"Keywords to search: {keywords}")
    print(f"Count of files: {len(files)}")
    print("=" * 80)
    print(f"Search using threads:")
    print(f"Number of threads: {min(10, len(files))}")

    start_time = time.time()
    result = multithreading_search(files, keywords)
    end_time = time.time()

    print("\nSearch results (Threading):")
    for keyword, occurrences in result.items():
        total_count = sum(count for _, count in occurrences)
        print(f"{keyword}: found in {total_count} places")

    print(f"Execution time (Threading): {end_time - start_time:.4f} seconds")
    logging.info(
        f"Multithreading search completed in {end_time - start_time:.4f} seconds"
    )
