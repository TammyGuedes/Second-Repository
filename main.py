import os
import shutil

source_folder = r'C:\Users\Usuario\Downloads'

categories = { 
    'Images':['.png','.jpg','.gif'],
    'Files': ['.pdf', '.xml'], 
    'Installers': ['.exe', '.msi']
             }

for category in categories:
    dest_path = os.path.join(source_folder, category)
    os.makedirs(dest_path, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isdir(file_path) or filename in categories:
        continue

    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    for category, extensions in categories.items():
        if file_extension in extensions:
            dest_file_path = os.path.join(source_folder, category, filename)
            shutil.move(file_path, dest_file_path)
            print(f'Moved: {filename} -> {category}')
            break