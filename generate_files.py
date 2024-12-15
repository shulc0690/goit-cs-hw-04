import os
import random
import string


def generate_random_text(words, min_length=600):
    text = " ".join(random.choices(string.ascii_letters + " ", k=min_length * 5))

    # Випадкове додавання слів з урахуванням позицій
    for word in words:
        num_occurrences = random.randint(
            1, 10
        )  # Випадкова кількість появи слова в тексті
        for _ in range(num_occurrences):
            pos = random.randint(0, len(text.split()) - 1)
            text = text.split()
            text[pos] = word
            text = " ".join(text)

    return text


def create_files_with_random_text(num_files, directory="random_texts", words=None):
    if words is None:
        words = ["OK", "Coca-Cola", "CORONA"]
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(num_files):
        file_path = os.path.join(directory, f"file_{i + 1}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(generate_random_text(words))


if __name__ == "__main__":
    num_files = 100000
    create_files_with_random_text(num_files)
    print(f"{num_files} files with random text have been created.")
