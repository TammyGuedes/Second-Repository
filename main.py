import os
import shutil

user_profile = os.environ['USERPROFILE']

source_folder = os.path.join(user_profile, 'Downloads')
destination_folder = os.path.join(user_profile, 'Documentos')

categories = { 
    'Images':['.png','.jpg','.gif'],
    'Files': ['.pdf', '.doc', '.xlsx', '.ods', '.xml', '.txt'], 
    'Installers': ['.exe', '.msi'],
    'Others': []
             }

for category in categories:
    dest_path = os.path.join(destination_folder, category)
    os.makedirs(dest_path, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isdir(file_path) or filename in categories:
        continue

    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    chosen_category = 'Others'
    for category, extensions in categories.items():
        if file_extension in extensions:
            dest_file_path = os.path.join(destination_folder, category, filename)
            shutil.move(file_path, dest_file_path)
            print(f'Moved: {filename} -> {category}')
            break