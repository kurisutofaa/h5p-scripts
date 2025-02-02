# h5p-scripts
To help create large amounts of h5p activities from csv data based on h5p templates I have

My goal overall is to get very comfortable with scripting so that i can apply it to all the different content types of h5p. 
To that end I am looking for help in understanding how things work rather than being given any code as such.

h5p files are a collection of JSON files. The main 3 directories I need to work with as far as I can tell are the content.json, images.json and h5p.json
I have a template 'Drag and Drop' h5p and a sample csv file called input.csv. 
There is a script that I tried to work through step by step with ChatGPT but it simply didn't work and I didn't know what else I was missing.
https://github.com/kurisutofaa/h5p-scripts/blob/main/content/script1.py 

I have my template Drag and Drop .h5p file here:
https://drive.google.com/file/d/1wGggELboKUZIDkkPlfniauWz2Bz_MNhH/view?usp=sharing

and this is an online editor that you can import it to see how the activity functions. It's German but the Chrome browser can translate. That's what I do.
https://videokonferenzintro.de/wp-admin/admin.php?page=h5p_new

I'll try and describe what the script needs to do as far as I can tell:
1. Read the first column of  input.csv 'Title' and create an entire replication of the template h5p using the Title as the name of the folder.
2. I guess I need to use shutil for this. 
3. Open up h5p.json and rename the title of the activity.
  
4. Basically 3 images should be given in a random order and the user drags and drops them into the correct dropbox.
5. There are 6 columns in input.csv showing the random order first and the next 3 show the correct order.
6. Need to go into content.json and take the next 3 columns of csv data 'Phoneme 1', 'Phoneme 2' and 'Phoneme 3' and map Phoneme 1 to line 28 placeholder1.png, Phoneme 2 to line 63 placeholder2.png and line 98 Phoneme 3 to placeholder3.png
7. I don't know what to call these things in the JSON, the correct terminology. I am now researching that. I guess they are object literals.
8. Need to go down to Line 121 dropZones and set correctElements to the correct order mapped from input.csv
9. Line 127 dropZones 0 should map to Correct 1. Line 145 dropZones 1 should map to Correct 2 and Line 163 dropZones 2 should map to Correct 3. 
10. Line 26 'path', the place where I will store the name of the png file, eg placeholder1.png -> fleece.png, there is a parameter called alt and I need to change that too. Maybe I could set it to the same name as the png?
11. I might need to set UUIDs wherever they are used. I'm not sure how much of a problem it would be to have them be duplicated across all copies of that activity, but I don't suppose it's hard to import uuid
    as it's a built in Python library, and generate UUIDs where needed.
12. I now have a script that can do the zipping up and changing the file name to .h5p. It also deletes the folder too.
   

I hope that makes some sense? I am open to any feedback whatsoever. Thank you. 

Other Notes
When zipping it is important to navigate inside the parent folder so that all the folders themselves are visible. Select all -> right click compress to zip them -> change extension to .h5p. To use the relative path, not the absolute path. I think that's the right way to describe it.
