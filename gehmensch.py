'''
This program will serve as an interface to my waterproof sony walkman.

It will allow:

- automatic playlist creation using every file in a particular folder
	This is the most important thing. it will make a playlist file using all the files in a particular folder
	on the walkman. The playlist file could have virtually the same name as the folder already there.

- transfer of files to the walkman
	this would be nice. it could simply overwrite files if they already exist on the walkman. or skip them. egal.
	to overwrite, when using the mv command, I just need the option -f

- deleting of files from the walkman
	this can be via prompt where a folder or file name must be entered
	or using a number menu with options to delete files / entire folders / or move into a folder
	this is not so important because it is easy enough to delete files manually 

'''

import os, eyed3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

os.system('cls' if os.name == 'nt' else 'clear')  # just clearing the screen

htext = ' SONY WALKMAN FILE MANAGER '
stars1 = '*' * ((80-len(htext))//2)
stars2 = '*' * (80-len(stars1) - len(htext))
print(f"\n{'*'*80}")
print(f"{stars1}{htext}{stars2}")
print(f"{'*'*80}")

# For now I assume the walkman will be found at:
# /media/jimbo/WALKMANNAMEHERE

# for the copying of files, to keep it simple I will just use a relative path.
# this gehmensch.py file should be in a folder named 'gehmensch'
# everything to be copied to the walkman should be in the folder:
# gehmensch/files2copy/

'''
folder_in = 'files2copy'
fol_list = []
for folder in os.walk(f"{folder_in}"):
	fol_list.append(folder[0])  # makes a list of every subfolder in the directory
print(f"Folders found: {fol_list}")

# ftypes = []  # list containing all file extensions found
# filextlist = []  # list containing all files with requested .ext with their full absolute path
for folder in fol_list:
	for myfile in os.listdir(folder):  # for every file in the particular folder
		if myfile.endswith(filext):
			filextlist.append(os.path.abspath(os.path.join(folder, myfile)))
		if myfile.find('.') not in [-1, 0]:  # -1 means there is no '.', 0 means it's the first character
			for i in range(len(myfile)):
				if myfile[i] == '.':
					myext = myfile[i:]
			if myext not in ftypes:
				ftypes.append(myext)
'''

# a simple option (maybe best to first implement this) is just to create playlists from given folders 
# already on the walkman
# so gehmensch.py could just be present in the root directory (or podcast directory may be better) of the walkman
# in this case:

# User prompt: enter folder name to create playlist

# so for testing, folder name:

# folder_in = 'podcasts/GrowthBusters'  	# because I think the .m3u files belong in the folder above 
										# podcasts, the root dir of the mp3 player
										# where this gehmensch.py file should be located

# folder_in = input(f"Enter relative path of folder to examine: ")
# folder_in = 'podcasts/GrowthBusters'
# folder_in = "podcasts/Everyone Is Right"
folder_in = 'podcasts/Under The Skin with Russell Brand'
print(f"\nFolder: {'./' + folder_in + '/'}")
filelistf = []
filelist = []

print(f"\nFile list: ")

for mfile in os.listdir(folder_in):
	print(f"{mfile}")
	# filelist.append(os.path.abspath(os.path.join(folder_in, mfile))) # this gives absolute path, not so relevant
	filelist.append(mfile)
	filelistf.append(os.path.relpath(os.path.join(folder_in, mfile))) # this looks very good!!!!
	# the above line looks to return the path relative to where the gehmensch.py script is run!!!
	# print(f"Relative path: {folder_in + '/' + mfile}")

for i in range(len(filelistf)):
	filenamef = filelistf[i]
	filename = filelist[i]
	try:
		audio = EasyID3(filenamef)
	except:
		print("Is this a valid audio file?\n****** FINISHED ******")
		quit()
	try:
		audio2 = MP3(filenamef)
	except:
		print("Is this a valid audio file?\n****** FINISHED ******")
		quit()

	print(f"\nFile: {filename}")
	try:
		print(f"Artist: {audio['artist']}")
	except:
		print(f"Artist unknown!")
		audio['artist'] = 'unknown'
	try:
		print(f"Album: {audio['album']}")
	except:
		print(f"Album unknown!")
		audio['album'] = 'unknown'
	try:
		print(f"Title: {audio['title']}")
	except:
		print(f"Title unknown!")
		audio['title'] = 'unknown'
	try:
		print(f"Time: {int(audio2.info.length)}")
	except:
		print(f"Time unknown!")

	# It depends on what file properties are actually displayed on the mp3 player 
	# as to what may be worth editing here.
	u_in = input(f"Change file properties (y/n): ").lower()
	if u_in == 'y':
		u_in_art = input(f"Change artist (y/n): ").lower()
		if u_in_art == 'y':
			audio['artist'] = input(f"Artist Name: ")
		u_in_alb = input(f"Change Album (y/n): ").lower()
		if u_in_alb == 'y':
			audio['album'] = input(f"Album: ")
		u_in_tit = input(f"Change Title (y/n): ").lower()
		if u_in_tit == 'y':
			audio['title'] = input(f"Title: ")
		audio.save()
		u_in_fname = input(f"Change Filename (y/n): ").lower()
		if u_in_fname == 'y':
		#new_fname = input(f"Enter New Filename (with correct .ext): ")
			os.rename(filenamef, os.path.relpath(folder_in) + '/' + input(f"Enter New Filename (with correct .ext): "))

# it may also be good to check that the file is of suitable audio format.
# maybe make a list that the file extension must belong to

'''
#EXTM3U

#EXTINF:105, Example artist - Example title
C:\Files\My Music\Example.mp3

#EXTINF:321, Example Artist2 - Example title2
C:\Files\My Music\Favorites\Example2.ogg

'''

# or just create a playlist for every folder? I don't think so, because there are probably too many folder
# but 

# before copying I can prompt the user whether files already present should be:
# overwritten: -f option
# prompt each time: -i option
# not overwritten: -n option

# how is the order of the playlists decided? I think it's alphabetical, numbers first
# this should be kept in mind if podcast files are to be renamed
# one could also rename the podcasts (or maybe more importantly folders) to have no spaces in the names

# in the folder on this computer:
# gehmensch/files2copy/
# are found files and potentially folders to be copied to the walkman.
# this would be like an 'image' to be transferred to the walkman
# ie 'Copy image from folder XXXXX'

# i could however look directly at the folders that rhythm box already uses.

# 