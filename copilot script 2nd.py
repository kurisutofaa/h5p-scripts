import os
import shutil
import csv
import json

template_directory = "/Users/tomomi/Documents/h5p, games, activities, pdfs/H5Ps/Word Scramble Unzips/Word Scramble w Correct"
destination_directory = "/Users/tomomi/Downloads"
input_csv = "/Users/tomomi/Downloads/input.csv"

# Phoneme to image mappings
phoneme_to_image = {
  "i:": "images/fleece.png",
  "ɪ": "images/kit.png",
  "e": "images/dress.png",
  "oʊ": "images/goal.png",
  "u:": "images/goose.png",
  "e:": "images/longdress.png",
  "ə": "images/comma.png",
  "ə:": "images/nurse.png",
  "ɔ:": "images/thought.png",
  "a": "images/trap.png",
  "ʌ": "images/strut.png",
  "ɑ:": "images/start.png",
  "ɒ": "images/lot.png",
  "eɪ": "images/face.png",
  "aɪ": "images/price.png",
  "ɔɪ": "images/choice.png",
  "əʊ": "images/goat.png",
  "ɪə": "images/near.png",
  "ɪ:": "images/longkit.png",
  "eə": "images/square.png",
  "tʃ": "images/ch.png",
  "dʒ": "images/dz.png",
  "p": "images/p.png",
  "b": "images/b.png",
  "d": "images/d.png",
  "t": "images/t.png",
  "k": "images/k.png",
  "g": "images/g.png",
  "f": "images/f.png",
  "v": "images/v.png",
  "θ": "images/theta.png",
  "ð": "images/eth.png",
  "s": "images/s.png",
  "z": "images/z.png",
  "ʃ": "images/sh.png",
  "ʒ": "images/zh.png",
  "m": "images/m.png",
  "n": "images/n.png",
  "ŋ": "images/ng.png",
  "h": "images/h.png",
  "l": "images/l.png",
  "r": "images/r.png",
  "w": "images/w.png",
  "j": "images/j.png",
  "ʔ": "images/glottal.png",
  "i": "images/happy.png",
  "x": "images/x.png"
}


# Function to get image path from phoneme
def get_image_path(phoneme):
    return phoneme_to_image.get(phoneme, None)

with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Get the title from the Title column
        title = row['Title']
        
        # Construct the new directory path in Downloads
        finished_copy = os.path.join(destination_directory, title)
        
        # Copy the template directory to the new directory
        new_folder = shutil.copytree(template_directory, finished_copy, dirs_exist_ok=True)
        print(f"Copied to: {new_folder}")
        
        # Path to the h5p.json file in the new directory
        h5p_json_path = os.path.join(new_folder, 'h5p.json')
        
        # Open and modify the h5p.json file
        if os.path.exists(h5p_json_path):
            with open(h5p_json_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            
            # Modify the title in the JSON data
            data['title'] = title
            
            # Save the modified JSON data back to the h5p.json file
            with open(h5p_json_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            
            print(f"Updated title in: {h5p_json_path}")
        
        # Path to the content.json file in the new directory
        content_json_path = os.path.join(new_folder, 'content', 'content.json')
        
        # Open and modify the content.json file
        if os.path.exists(content_json_path):
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