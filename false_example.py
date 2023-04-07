import os
import shutil
from typing import List


def check_source_folder(source_folder: str) -> bool:
    """
    Проверка существования исходной папки
    """
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не существует.")
        return False
    return True


def create_destination_folder(destination_folder: str) -> None:
    """
    Создание целевой папки, если она не существует
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


def get_image_files(source_folder: str, image_extensions: List[str]) -> List[str]:
    """
    Сбор списка файлов изображений
    """
    image_files = []
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)) and os.path.splitext(filename)[1] in image_extensions:
            image_files.append(filename)
    return image_files


def copy_images(source_folder: str, destination_folder: str, image_files: List[str]) -> None:
    """
    Копирование файлов изображений из исходной папки в целевую папку
    """
    for filename in image_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)


def collect_images(source_folder: str, destination_folder: str, image_extensions: List[str]) -> None:
    """
    Функция для сбора изображений из указанной папки и копирования их в указанную папку
    """
    if not check_source_folder(source_folder):
        return
    create_destination_folder(destination_folder)
    image_files = get_image_files(source_folder, image_extensions)
    copy_images(source_folder, destination_folder, image_files)
    print(
        f"Все изображения ({len(image_files)}) были успешно скопированы в папку назначения.")


if __name__ == '__main__':
    sourse_folder = r'E:\Пользователи\mike\Рабочий стол'
    destination_folder = r'E:\Пользователи\mike\Рабочий стол\All_images'
    image_extensions: List[str] = ['.jpg', '.jpeg', '.png', '.bmp']
    collect_images(sourse_folder, destination_folder, image_extensions)

"""Код можно разделить на более мелкие функции, но в данном случае это может быть избыточно и не даст значительных преимуществ.
Однако, если не соблюдать принцип единственной ответственности и разделять функцию на множество более мелких функций,
можно представить следующий вариант разделения кода:
    check_source_folder(source_folder: str) -> bool - функция для проверки существования исходной папки
    create_destination_folder(destination_folder: str) -> None - функция для создания целевой папки, если она не существует
    get_image_files(source_folder: str, image_extensions: List[str]) -> List[str] - функция для сбора списка файлов изображений
    copy_images(source_folder: str, destination_folder: str, image_files: List[str]) -> None - функция для копирования файлов изображений из исходной папки в целевую папку
Каждая из этих функций будет выполнять только одно конкретное действие, но в данном случае такое разделение будет избыточным и усложнит код, не давая значительных преимуществ."""
