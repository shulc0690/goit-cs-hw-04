# goit-cs-hw-04
Конкурентність та паралелізм

Перед початком роботи:
1. Версія **Python: >=3.11**
2. Cтворюємо віртуальне середовище (Python: >=3.11) `.env`: `python -m venv .env`
3. Активуємо (відповідно до своєї ОС): `.env\Scripts\activate`
4. Інсталюємо залежності: `pip install -r requirements.txt`
5. По завершенню роботи деактивовуємо: `.env\Scripts\deactivate`
6. Сгенерувати файли запустивши `generate_files.py`

Результат обробки файлів:
```bash
Keywords to search: ['OK', 'Coca-Cola', 'CORONA']
Count of files: 10000
================================================================================
Search using threads:
Number of threads: 10

Search results (Threading):
OK: found in 54712 places
Coca-Cola: found in 54729 places
CORONA: found in 54593 places
Execution time (Threading): 2.4991 seconds


Keywords to search: ['OK', 'Coca-Cola', 'CORONA']
Count of files: 10000
================================================================================
Search using multiprocessing:

Search results (Multiprocessing):
OK: found in 54712 places
Coca-Cola: found in 54729 places
CORONA: found in 54593 places
Execution time (Multiprocessing): 3.3873 seconds
```