# Code for concatenate text files that are in the same folder
# Leonidas Carrasco-Letelier
# lcarrasco@inia.org.uy

import os

def concatenate_txt_files(folder_path, output_filename):
    """
    Concatenates the content of all .txt files in a folder into a single output file.

    Args:
        folder_path (str): The path to the folder containing the .txt files.
        output_filename (str): The name of the file where the concatenated content will be saved.
    """
    # Build the full path for the output file
    output_filepath = os.path.join(folder_path, output_filename)

    print(f"Looking for .txt files in folder: {folder_path}")

    # Open the output file in write mode ('w') to ensure it's empty at the start
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        # Iterate over each file in the specified folder
        for filename in os.listdir(folder_path):
            # Check if the file has a .txt extension and is not the output file itself
            if filename.endswith('.txt') and filename != output_filename:
                full_file_path = os.path.join(folder_path, filename)
                print(f"Concatenating file: {filename}")
                try:
                    # Open each input file in read mode ('r')
                    with open(full_file_path, 'r', encoding='utf-8') as input_file:
                        content = input_file.read()
                        # Write the content to the output file, followed by a newline for separation
                        output_file.write(content + '\n')
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    print("\nProcess finished. All files have been concatenated into: " + output_filename)

# --- SCRIPT CONFIGURATION ---
# Set the path of the folder containing your .txt files.
# The '.' means the script will look in the current directory where it's being executed.
# Change this if your files are in a different location.
folder_to_process = '.'

# Define the name of the output file where the result will be saved
result_filename = 'all_files.txt'

# Run the function to start the process
concatenate_txt_files(folder_to_process, result_filename)