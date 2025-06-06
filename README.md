# GOIT Algorithm Homework 03

## Task 1 — File Sorter by Extension

Скрипт рекурсивно копіює всі файли з вихідної директорії до директорії призначення, сортує їх за розширенням у відповідні підпапки.

### Запуск:

```bash
python3 homework-algo-03.py ./input ./output
```

- `./input` — вихідна директорія з файлами
- `./output` — директорія призначення
- Якщо другий аргумент не вказано — використовується `./dist` за замовчуванням

---

## Task 2 — Koch Snowflake Fractal

Скрипт будує фрактал “сніжинку Коха” з заданим рівнем рекурсії.

### Запуск:

```bash
python3 homework-algo-03-koch-snowflake.py
```

Приклад вводу:

```
Введіть рівень рекурсії (0-6): 3
```

Відкриється графічне вікно з фракталом.

### Вимоги:

- Python 3.x
- tkinter (вбудовано в стандартний Python для Windows/Linux, для macOS можна встановити через Homebrew: `brew install python-tk`)
