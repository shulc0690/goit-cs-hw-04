# goit-cs-hw-04
Конкурентність та паралелізм

Перед початком роботи:
1. Версія **Python: >=3.11**
2. Cтворюємо віртуальне середовище (Python: >=3.11) `.env`: `python -m venv .env`
3. Активуємо (відповідно до своєї ОС): `.env\Scripts\activate`
4. Інсталюємо залежності: `pip install -r requirements.txt`
5. По завершенню роботи деактивовуємо: `.env\Scripts\deactivate`
6. Сгенерувати файли для тесту:  `generate_files.py`

Результат обробки файлів:
```bash
Keywords to search: ['OK', 'Coca-Cola', 'CORONA']
Count of files: 100000
================================================================================
Search using threads:
Number of threads: 10

Search results (Threading):
OK: found in 547564 places
Coca-Cola: found in 549446 places
CORONA: found in 549254 places
Execution time (Threading): 75.5222 seconds


Keywords to search: ['OK', 'Coca-Cola', 'CORONA']
Count of files: 100000
================================================================================
Search using multiprocessing:
Number of processers: 10

Search results (Multiprocessing):
OK: found in 547564 places
Coca-Cola: found in 549446 places
CORONA: found in 549254 places
Execution time (Multiprocessing): 2.9551 seconds
```