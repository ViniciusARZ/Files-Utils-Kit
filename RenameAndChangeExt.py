import os
import re

def rename_files(folder_path, keyword):
    # Pattern to match date formats with or without defined extensions (jpg, pdf and jpeg, add others if necessary)
    pattern = re.compile(r'(\d{2})[. ](\d{2,4})(.*?)(\.jpg|\.jpeg|\.pdf|)$', re.IGNORECASE)
    already_correct_pattern_jpg = re.compile(fr'{re.escape(keyword)} \d{{4}}-\d{{2}}\.jpg$', re.IGNORECASE)
    already_correct_pattern_pdf = re.compile(fr'{re.escape(keyword)} \d{{4}}-\d{{2}}\.pdf$', re.IGNORECASE)

    for filename in sorted(os.listdir(folder_path)):
        try:
            # Skip files that are already correctly named
            if already_correct_pattern_jpg.match(filename) or already_correct_pattern_pdf.match(filename):
                print(f'Skipped (already correct): {filename}')
                continue

            match = pattern.search(filename)
            if match:
                month, year, extra, extension = match.groups()
                
                # Adjust year to YYYY format if necessary
                year = f'20{year}' if len(year) == 2 else year

                # Determine the correct extension
                if '.pdf' in extension.lower():
                    new_ext = '.pdf'  # Keep original .pdf extension
                else:
                    new_ext = '.jpg'  # Default to .jpg for other cases (adjust this if necessary)

                new_name = f"{keyword} {year}-{month}{new_ext}"
                
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {new_name}')
            else:
                print(f'Skipped: {filename}')
        except Exception as e:
            print(f"Error with file '{filename}': {e}")

# calling main for user input
if __name__ == "__main__":
    print("File Naming Pattern: 'KEYWORD YYYY-MM.ext' ")
    folder_path = input("Enter the path of the folder: ")
    keyword = input("Enter the keyword: ")
    rename_files(folder_path, keyword)