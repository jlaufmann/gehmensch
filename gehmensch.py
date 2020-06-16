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

# so far this is more just an audio property editing script and nothing to do with the walkman interface.

######################### stuff removed from here!!!!!!!!!!!!!!!!!#################################

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

# Playlist file name could be just that of the folder, or user defined.

'''
#EXTM3U

#EXTINF:105, Example artist - Example title
C:\Files\My Music\Example.mp3

#EXTINF:321, Example Artist2 - Example title2
C:\Files\My Music\Favorites\Example2.ogg

'''

# before copying I can prompt the user whether files already present should be:
# overwritten: -f option
# prompt each time: -i option
# not overwritten: -n option

# how is the order of the playlists decided? I think it's alphabetical, numbers first
# this should be kept in mind if podcast files are to be renamed

# in the folder on this computer:
# gehmensch/files2copy/
# are found files and potentially folders to be copied to the walkman.
# this would be like an 'image' to be transferred to the walkman
# ie 'Copy image from folder XXXXX'

# i could however look directly at the folders that rhythm box already uses.

# 