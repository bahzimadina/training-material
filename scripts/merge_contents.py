import os
import sys

def merge_files(folder_path, output_filename, prefix_filter):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if f.startswith(prefix_filter) and f.endswith('.md')]
    files.sort() # Ensure order (e.g., slide_topik1, slide_topik2)
    
    if not files:
        print(f"No files found starting with '{prefix_filter}' in '{folder_path}'.")
        return

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for i, filename in enumerate(files):
            with open(os.path.join(folder_path, filename), 'r') as infile:
                outfile.write(infile.read())
                # Only add separator if it's not the last file
                if i < len(files) - 1:
                    outfile.write("\n\n---\n\n") 
    print(f"Successfully merged {len(files)} files into {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_contents.py <folder_path> <output_filename> <prefix_filter>")
    else:
        merge_files(sys.argv[1], sys.argv[2], sys.argv[3])
