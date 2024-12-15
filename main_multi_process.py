import multiprocessing
import os
import time
import logging
from pathlib import Path

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def search_keywords_in_file(file_path, keywords):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for keyword in keywords:
                count = content.count(keyword)
                if count > 0:
                    results.append((keyword, file_path, count))
                    logging.info(
                        f"Keyword '{keyword}' found {count} times in {file_path}"
                    )
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
    return results


def multiprocessing_search(files, keywords):
    with multiprocessing.Pool(os.cpu_count()) as pool:
        results = pool.starmap(
            search_keywords_in_file, [(file, keywords) for file in files]
        )
    flattened_results = [
        item for sublist in results for item in sublist
    ]  # Flatten list of lists
    return flattened_results


def get_files_from_directory(directory):
    return [str(file) for file in Path(directory).rglob("*.txt")]


if __name__ == "__main__":
    directory = "random_texts"  # Директорія з файлами
    files = get_files_from_directory(directory)
    keywords = ["OK", "Coca-Cola", "CORONA"]  # Слова для пошуку

    print(f"Keywords to search: {keywords}")
    print(f"Count of files: {len(files)}")
    print("=" * 80)
    print(f"Search using multiprocessing:")
    print(f"Number of processers: {min(10, len(files))}")

    start_time = time.time()
    result = multiprocessing_search(files, keywords)
    end_time = time.time()

    print("\nSearch results (Multiprocessing):")
    keyword_counts = {}
    for keyword, file_path, count in result:
        if keyword not in keyword_counts:
            keyword_counts[keyword] = 0
        keyword_counts[keyword] += count

    for keyword, total_count in keyword_counts.items():
        print(f"{keyword}: found in {total_count} places")

    print(f"Execution time (Multiprocessing): {end_time - start_time:.4f} seconds")
    logging.info(
        f"Multiprocessing search completed in {end_time - start_time:.4f} seconds"
    )
