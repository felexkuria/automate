import os
import shutil

# Define the paths
downloads_folder = os.path.expanduser('~/Downloads')
mp3_folder = os.path.join(downloads_folder, 'MP3_Files')
pdf_folder = os.path.join(downloads_folder, 'PDF_Files')

# Create folders if they don't exist
os.makedirs(mp3_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)

# Function to move files to the correct folders
def organize_files():
    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move MP3 files
        if file_name.lower().endswith('.mp3'):
            shutil.move(file_path, os.path.join(mp3_folder, file_name))
            print(f'Moved {file_name} to MP3_Files.')

        # Move PDF files
        elif file_name.lower().endswith('.pdf'):
            shutil.move(file_path, os.path.join(pdf_folder, file_name))
            print(f'Moved {file_name} to PDF_Files.')

if __name__ == '__main__':
    organize_files()

