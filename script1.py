import os
import shutil
import csv

# Define the path to the template directory (replace with your actual path)
template_directory = '/Users/tomomi/Downloads/Word Scramble 3 Phonemes'

# Define the output directory (we're using Downloads in this example)
output_directory = os.path.expanduser('~/Downloads')

# Path to the input CSV file (replace with your actual file path)
csv_file_path = '/Users/tomomi/Downloads/Word Scramble 3 Phonemes/content/input.csv'

# Read the CSV file and process each row
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get the title from the Title column
        title = row['Title']
        
        # Construct the new directory path in Downloads
        new_directory = os.path.join(output_directory, title)
        
        # Check if the directory already exists, if not, create it
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        
        # Copy the entire template directory into the new directory
        try:
            shutil.copytree(template_directory, new_directory)
            print(f"Successfully copied template to: {new_directory}")
        except Exception as e:
            print(f"Error copying template to {new_directory}: {e}")
