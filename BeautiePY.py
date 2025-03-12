import os
import shutil
import re

path = "/storage/emulated/0/Download/AlmasMovie"  # Adjust this path if needed
valid_extensions = (".mkv", ".mp4", ".avi", ".srt", ".ass", ".sub")

movies_folder = os.path.join(path, "Movies")  # Common folder for movies
tv_shows_folder = os.path.join(path, "Series")  # Folder for TV shows

os.makedirs(movies_folder, exist_ok=True)

for file in os.listdir(path):
    if file.startswith(".") or not file.endswith(valid_extensions):
        continue  # Skip hidden/system/unrelated files

    # Combined regex for TV shows (handles prefixes and separators)
    tv_show_match = re.match(r"[^\w]*([A-Za-z0-9\.\-\s_]+?)[_\.\-\s](S\d{1,2}E\d{1,2}|E\d{1,2})", file, re.IGNORECASE)

    if tv_show_match:
        # Extract the series name from the matched group
        show_name = tv_show_match.group(1).strip().replace(" ", ".").replace("_", ".")
        folder_path = os.path.join(tv_shows_folder, show_name)
    else:
        # Treat anything else as a movie
        folder_path = movies_folder

    os.makedirs(folder_path, exist_ok=True)
    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))