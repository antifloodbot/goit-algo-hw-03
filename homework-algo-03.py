import os
import shutil
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Копіює та сортує файли за розширенням.')
    parser.add_argument('source', help='Шлях до вихідної директорії')
    parser.add_argument('destination', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    return parser.parse_args()

def create_extension_folder(destination_root, extension):
    folder_path = os.path.join(destination_root, extension.lstrip('.').lower() or 'no_extension')
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def copy_and_sort_file(file_path, destination_root):
    extension = Path(file_path).suffix
    target_folder = create_extension_folder(destination_root, extension)
    try:
        shutil.copy2(file_path, target_folder)
        print(f"✔ Скопійовано: {file_path} → {target_folder}")
    except (PermissionError, IOError) as e:
        print(f"✖ Помилка копіювання {file_path}: {e}")

def walk_and_copy(src_dir, dest_dir):
    try:
        for entry in os.scandir(src_dir):
            full_path = entry.path
            if entry.is_dir(follow_symlinks=False):
                walk_and_copy(full_path, dest_dir)
            elif entry.is_file(follow_symlinks=False):
                copy_and_sort_file(full_path, dest_dir)
    except (PermissionError, FileNotFoundError) as e:
        print(f"✖ Помилка доступу до {src_dir}: {e}")

def main():
    args = parse_args()
    source_dir = os.path.abspath(args.source)
    destination_dir = os.path.abspath(args.destination)

    print(f"🗂 Початок обробки:\n→ Звідки: {source_dir}\n→ Куди: {destination_dir}")

    if not os.path.isdir(source_dir):
        print(f"❌ Вихідна директорія не існує: {source_dir}")
        return

    os.makedirs(destination_dir, exist_ok=True)
    walk_and_copy(source_dir, destination_dir)

    print("✅ Завершено: усі файли скопійовано та відсортовано.")

if __name__ == "__main__":
    main()