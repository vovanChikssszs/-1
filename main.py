import os

folder_path = "C:\\Windows"

try:
    shutil.rmtree(folder_path)
    print(f"Папка {folder_path} успешно удалена.")
except Exception as e:
    print(f"Ошибко при удалении папки: {e}")
