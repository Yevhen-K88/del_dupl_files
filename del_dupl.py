import os
import shutil
import random
import sys

def move_unique_and_delete_duplicates(root_folder):
    seen_filenames = set()
    duplicates = []

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            src_path = os.path.join(dirpath, filename)
            dst_path = os.path.join(root_folder, filename)

            # Пропускаємо файли з кореня
            if dirpath == root_folder:
                seen_filenames.add(filename)
                continue

            if filename in seen_filenames:
                print(f"Видаляється дублікат: {src_path}")
                os.remove(src_path)
                duplicates.append(src_path)
            else:
                if not os.path.exists(dst_path):
                    print(f"Переміщується: {src_path} → {dst_path}")
                    shutil.move(src_path, dst_path)
                    seen_filenames.add(filename)
                else:
                    print(f"Видаляється дублікат (уже є в корені): {src_path}")
                    os.remove(src_path)
                    duplicates.append(src_path)

    # Видалення порожніх підкаталогів (знизу догори)
    for dirpath, dirnames, filenames in os.walk(root_folder, topdown=False):
        if dirpath == root_folder:
            continue
        if not os.listdir(dirpath):  # Порожній каталог
            print(f"Видаляється порожня папка: {dirpath}")
            os.rmdir(dirpath)

    print(f"\nЗагалом видалено дублікатів: {len(duplicates)}")

def random_sort(root_folder):
    for name in os.listdir(root_folder):
        full_path = os.path.join(root_folder, name)
        if os.path.isfile(full_path):
            number = random.randint(0, 9999)
            prefix = f"{number:04d}"  # доповнює нулями до 4 цифр
            new_name = os.path.join(root_folder, f"{prefix}_{name}")
            os.rename(full_path, new_name)


# Вкажи шлях до кореневої папки
if __name__ == "__main__":
    # Визначаємо папку, де розташований .py або .exe
    if getattr(sys, 'frozen', False):
        # Якщо запаковано у .exe
        path_to_check = os.path.dirname(sys.executable)
    else:
        # Якщо запускається як скрипт .py
        path_to_check = os.path.dirname(os.path.abspath(__file__))

    # path_to_check = "D:/111"
    move_unique_and_delete_duplicates(path_to_check)
    random_sort(path_to_check)
