import os
import shutil

user_profile = os.path.expanduser("~")
source_folder = os.path.join(user_profile, 'Downloads')
destination_folder = os.path.join(user_profile, 'Documents')
movedtotal = 0

categories = { 
    'Images':['.png','.jpg','.gif', '.webp', '.jpeg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Files': ['.pdf', '.doc', '.xlsx', '.ods', '.xml', '.txt', '.docx', '.pptx'], 
    'Installers': ['.exe', '.msi', '.appx', '.msix', '.dmg', '.pkg'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar.gz', '.gz', '.bz2']
             }



for category in categories:
    dest_path = os.path.join(destination_folder, category)
    os.makedirs(dest_path, exist_ok=True)



for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isdir(file_path) or filename.startswith('.'):
        continue
    if filename.lower().endswith('.tar.gz'):
        file_extension = '.tar.gz'
    else:
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()



    for category, extensions in categories.items():
        if file_extension in extensions:
            dest_file_path = os.path.join(destination_folder, category, filename)
            original_filename = filename
            if os.path.exists(dest_file_path):
                if filename.lower().endswith('.tar.gz'):
                    name = filename[:-7]
                    ext = '.tar.gz'
                else:
                    name, ext = os.path.splitext(filename)

                counter = 1
                while os.path.exists(dest_file_path):
                    new_filename = f'{name}_{counter}{ext}'
                    dest_file_path = os.path.join(destination_folder, category, new_filename)
                    counter += 1

                filename = new_filename

            try:
                shutil.move(file_path, dest_file_path)
                print(f'Moved: {filename} -> {category}')
                movedtotal += 1
            except PermissionError:
                print(f'Error! File: {original_filename} is currently being used by another application.')  

            except Exception as e:
                print(f'Unexpected error while moving {original_filename}: {e}')  
            break
print(f'Total moved files: {movedtotal}')
