import os
import shutil
import sys

# Define the file types for organization
file_types = {
    'MP3_Files': ('.mp3',),
    'PDF_Files': ('.pdf',),
    'Image_Files': ('.heic', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'),
    'Video_Files': ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.mpg'),
    'Document_Files': ('.docx', '.xlsx', '.pptx', '.txt', '.rtf', '.csv', '.md', '.odt', '.pages')
}

# Available folders to organize
available_folders = {
    '1': ('Downloads', os.path.expanduser('~/Downloads')),
    '2': ('Desktop', os.path.expanduser('~/Desktop')),
    '3': ('Both', [os.path.expanduser('~/Downloads'), os.path.expanduser('~/Desktop')])
}

# Function to create necessary organization folders in the specified location
def create_organization_folders(base_folder):
    folders = {folder: os.path.join(base_folder, folder) for folder in file_types}
    for path in folders.values():
        os.makedirs(path, exist_ok=True)
    return folders

# Function to organize files efficiently
def organize_files(target_folder):
    print(f"Organizing files in {target_folder}...")
    folders = create_organization_folders(target_folder)
    
    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)
        if not os.path.isfile(file_path):  # Skip directories
            continue

        for folder, extensions in file_types.items():
            if file_name.lower().endswith(extensions):
                target_subfolder = folders[folder]
                
                # Handle screenshots separately
                if folder == 'Image_Files' and file_name.lower().startswith("screenshot"):
                    target_subfolder = os.path.join(target_subfolder, 'Screenshots')
                    os.makedirs(target_subfolder, exist_ok=True)
                
                shutil.move(file_path, os.path.join(target_subfolder, file_name))
                print(f'Moved {file_name} to {target_subfolder}')
                break  # Stop checking other types once matched

def show_menu():
    print("\nFile Organizer - Choose which folder(s) to organize:")
    print("1. Downloads Folder")
    print("2. Desktop Folder")
    print("3. Both Folders")
    print("0. Exit")
    
    choice = input("\nEnter your choice (0-3): ")
    
    if choice == '0':
        print("Exiting program.")
        sys.exit(0)
    elif choice in available_folders:
        selected = available_folders[choice]
        if choice == '3':  # Both folders
            for folder in selected[1]:
                organize_files(folder)
        else:
            organize_files(selected[1])
    else:
        print("Invalid choice. Please try again.")
        show_menu()

if __name__ == "__main__":
    show_menu()

