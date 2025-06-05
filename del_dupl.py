import os


def delete_duplicate_filenames(root_folder):
    seen_filenames = set()
    duplicates = []

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename in seen_filenames:
                filepath = os.path.join(dirpath, filename)
                print(f"Видаляється дублікат: {filepath}")
                os.remove(filepath)
                duplicates.append(filepath)
            else:
                seen_filenames.add(filename)

    print(f"\nЗагалом видалено дублікатів: {len(duplicates)}")


# Заміни цей шлях на свій
if __name__ == "__main__":
    path_to_check = "шлях/до/твоєї/папки"
    delete_duplicate_filenames(path_to_check)
