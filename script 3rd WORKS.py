import os
import shutil
import csv
import json

template_directory = "/Users/tomomi/Documents/h5p, games, activities, pdfs/H5Ps/Word Scramble Unzips/Word Scramble w Correct"
destination_directory = "/Users/tomomi/Downloads"
input_csv = "/Users/tomomi/Downloads/input.csv"

# Phoneme to image mappings
phoneme_to_image = {
    "phoneme1": "images/image1.png",
    "phoneme2": "images/image2.png",
    "phoneme3": "images/image3.png",
    # Add all your phoneme to image mappings here
}

# Function to get image path from phoneme
def get_image_path(phoneme):
    return phoneme_to_image.get(phoneme, None)

try:
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Print column names for debugging
        print(f"CSV columns: {reader.fieldnames}")
        
        for row in reader:
            # Get the title from the Title column
            title = row['Title']
            print(f"Processing title: {title}")
            
            # Construct the new directory path in Downloads
            finished_copy = os.path.join(destination_directory, title)
            
            # Copy the template directory to the new directory
            try:
                new_folder = shutil.copytree(template_directory, finished_copy, dirs_exist_ok=True)
                print(f"Copied to: {new_folder}")
            except Exception as e:
                print(f"Error copying directory: {e}")
                continue
            
            # Path to the h5p.json file in the new directory
            h5p_json_path = os.path.join(new_folder, 'h5p.json')
            
            # Open and modify the h5p.json file
            if os.path.exists(h5p_json_path):
                try:
                    with open(h5p_json_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                    
                    # Modify the title in the JSON data
                    data['title'] = title
                    
                    # Save the modified JSON data back to the h5p.json file
                    with open(h5p_json_path, 'w', encoding='utf-8') as json_file:
                        json.dump(data, json_file, ensure_ascii=False, indent=4)
                    
                    print(f"Updated title in: {h5p_json_path}")
                except Exception as e:
                    print(f"Error updating h5p.json: {e}")
            else:
                print(f"h5p.json not found in: {new_folder}")
            
            # Path to the content.json file in the new directory
            content_json_path = os.path.join(new_folder, 'content', 'content.json')
            
            # Open and modify the content.json file
            if os.path.exists(content_json_path):
                try:
                    with open(content_json_path, 'r', encoding='utf-8') as content_file:
                        content_data = json.load(content_file)
                    
                    # Update image paths based on phonemes
                    phoneme_columns = ['Phoneme 1', 'Phoneme 2', 'Phoneme 3']
                    for i, phoneme_column in enumerate(phoneme_columns):
                        phoneme = row[phoneme_column]
                        image_path = get_image_path(phoneme)
                        if image_path:
                            # Assuming the structure of content.json matches the provided context
                            content_data['images'][i]['file']['path'] = image_path
                    
                    # Save the modified JSON data back to the content.json file
                    with open(content_json_path, 'w', encoding='utf-8') as content_file:
                        json.dump(content_data, content_file, ensure_ascii=False, indent=4)
                    
                    print(f"Updated image paths in: {content_json_path}")
                except Exception as e:
                    print(f"Error updating content.json: {e}")
            else:
                print(f"content.json not found in: {new_folder}")
except Exception as e:
    print(f"Error reading CSV file: {e}")