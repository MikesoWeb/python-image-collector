import os
import shutil
from typing import List


def collect_images(source_folder: str, destination_folder: str, image_extensions: List[str]) -> None:
    # Проверяем, что исходная папка существует
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не существует.")
        return

    # Проверяем, что целевая папка существует или создаем ее
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Собираем изображения
    image_files = []
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)) and os.path.splitext(filename)[1] in image_extensions:
            image_files.append(filename)

    # Копируем изображения в целевую папку
    for filename in image_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)

    print(
        f"Все изображения ({len(image_files)}) были успешно скопированы в папку назначения.")


if __name__ == '__main__':
    sourse_folder = r'E:\Пользователи\mike\Рабочий стол'
    destination_folder = r'E:\Пользователи\mike\Рабочий стол\All_images'
    image_extensions: List[str] = ['.jpg', '.jpeg', '.png', '.bmp']
    collect_images(sourse_folder, destination_folder, image_extensions)


"""В данном примере кажется можно выделить функционал создания, проверки существования в разные функции, 
тем самым соблюдая Принцип единственной ответственности SRP- Single Responsibility Principle (SOLID). 
В нем говорится что каждый объект или функция должы иметь только одну ответственность и заниматься своим делом.
Это может снизить связанность между различными компонентами системы, что упростит поддержку, тестирование, расширения кода.


  Но в нашем примере реализация является простой и короткой и дополнительное разделение на несколько функций 
  будет способствовать увеличению сложности кода и тем самым нарушением принципа KISS - Keep It Simple, Stupid, 
  который говорит что любая система не должна иметь лишней сложности, если это не обязательно. Важно чтобы программный код
 был простым и легко читаемым для человека"""
