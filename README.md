# BeautiePY

---

**Instructions for Using BeautiePY Script**

1. **Purpose**  
   This script organizes your media files into separate folders for TV shows and movies based on their filenames.

2. **Required Setup**  
   - Install Python 3.x on your system.
   - Place all your video and subtitle files in the folder specified by the `path` variable in the script.
   - Make sure the file types match these extensions:
     - `.mkv`, `.mp4`, `.avi`, `.srt`, `.ass`, `.sub`

3. **Custom Configuration**  
   - Open the script in a text editor.
   - Modify the `path` variable to point to the folder containing your media files.
     Example:  
     ```python
     path = "/path/to/your/files"
     ```
   - Adjust the `movies_folder` and `tv_shows_folder` variables to rename or change the default folder structure for organized files.

4. **How It Works**  
   - The script identifies TV shows based on filenames containing patterns like `S01E01` or `E03`.
   - All other files are treated as movies.
   - TV shows are moved into a `Series/ShowName/` folder.
   - Movies are moved into a shared `Movies/` folder.

5. **Running the Script**  
   - Open a terminal or command prompt.
   - Navigate to the folder where the script is saved.
   - Run the script using the following command:
     ```
     python script_name.py
     ```

6. **Results**  
   - Files will be moved and organized in the following structure:
     ```
     Series/
     ├── ShowName/
     │   ├── ShowName.S01E01.mkv
     │   └── ShowName.S01E02.srt
     Movies/
     ├── MovieName.mkv
     ├── AnotherMovie.mp4
     ```

7. **Notes and Limitations**  
   - Files that don’t match the TV show regex pattern will be moved to the `Movies` folder.
   - This script does not distinguish between completed and incomplete downloads, so ensure all files are complete before running the script.

8. **Error Handling**  
   - If the script encounters an issue (e.g., missing permissions or unreadable files), it will log an error message and skip the file.

9. **Customization**  
   - You can modify the `valid_extensions` variable to include other file types as needed.
   - Advanced users can add new regex patterns for different naming conventions in the `tv_show_match` regex.

10. **Contact/Help**  
    For further help or issues, modify the script or refer to the Python documentation.

---
