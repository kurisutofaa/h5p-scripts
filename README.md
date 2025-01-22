# h5p-scripts
To help create large amounts of h5p activities from csv data based on h5p templates I have

h5p files are a collection of JSON files. The main 3 directories I need to work with as far as I can tell are the content.json, images.json and h5p.json
I have a template 'Drag and Drop' h5p and a sample csv file called input.csv. 
There is a script that I tried to work through step by step with ChatGPT but it simply didn't work and I didn't know what else I was missing.

I have my template Drag and Drop .h5p file here:
https://drive.google.com/file/d/1wGggELboKUZIDkkPlfniauWz2Bz_MNhH/view?usp=sharing

and this is an online editor that you can import it to see how the activity functions. It's German but the Chrome browser can translate. That's what I do.
https://videokonferenzintro.de/wp-admin/admin.php?page=h5p_new

I'll try and describe what the script needs to do as far as I can tell:
1. Read the first column of the csv 'Title' and create an entire replication of the template h5p using the Title as the name of the folder.
2. I guess I need to use shutil for this. 
3. Open up h5p.json and rename the title of the activity.
  
4. Basically 3 images should be given in a random order and the user drags and drops them into the correct dropbox.
5. There are 6 columns in input.csv showing the random order first and the next 3 show the correct order.
6. Need to go into content.json and take the next 3 columns of csv data 'Phoneme 1', 'Phoneme 2' and 'Phoneme 3' and map Phoneme 1 to placeholder1.png, Phoneme 2 to placeholder2.png and 3 to 3.
7. 
