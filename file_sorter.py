import os
import shutil
import sys


def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(description="Копіює файли та сортує за розширеннями.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення")
    return parser.parse_args()


def copy_and_sort_files(src_dir, dest_dir):
    try:

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir)
            else:
    
                file_extension = os.path.splitext(item)[-1].lower().strip(".")
                if not file_extension:
                    file_extension = "no_extension"

                extension_folder = os.path.join(dest_dir, file_extension)
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                shutil.copy2(item_path, extension_folder)
                print(f"Скопійовано: {item} -> {extension_folder}")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    args = parse_arguments()

    source_dir = os.path.abspath(args.source)
    destination_dir = os.path.abspath(args.destination)

    if not os.path.exists(source_dir):
        print(f"Помилка: Вихідна директорія '{source_dir}' не існує.")
        sys.exit(1)

    copy_and_sort_files(source_dir, destination_dir)
    print(f"Копіювання завершено. Файли збережені в '{destination_dir}'.")
