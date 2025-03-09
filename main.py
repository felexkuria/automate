import os
import shutil

# Define the paths
downloads_folder = os.path.expanduser('~/Downloads')
file_types = {
    'MP3_Files': ('.mp3',),
    'PDF_Files': ('.pdf',),
    'Image_Files': ('.heic', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'),
    'Video_Files': ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg'),
    'Document_Files': ('.docx', '.xlsx', '.pptx', '.txt', '.rtf', '.csv', '.md', '.odt', '.pages')
}

# Create necessary folders
folders = {folder: os.path.join(downloads_folder, folder) for folder in file_types}
for path in folders.values():
    os.makedirs(path, exist_ok=True)

# Function to organize files efficiently
def organize_files():
    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)
        if not os.path.isfile(file_path):  # Skip directories
            continue

        for folder, extensions in file_types.items():
            if file_name.lower().endswith(extensions):
                target_folder = folders[folder]
                
                # Handle screenshots separately
                if folder == 'Image_Files' and file_name.lower().startswith("screenshot"):
                    target_folder = os.path.join(target_folder, 'Screenshots')
                    os.makedirs(target_folder, exist_ok=True)
                
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f'Moved {file_name} to {target_folder}')
                break  # Stop checking other types once matched

if __name__ == "__main__":
    organize_files()

