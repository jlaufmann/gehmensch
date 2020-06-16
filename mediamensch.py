'''

This script examines every (media) file in a given folder and enables quick
editing of the media file via the command line.

it was written before gehmensch, in order to prepare files for transfer to 
the sony walkman.


'''

import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def findext(fname):
	if fname.find('.') == -1:
		fext = ''
	else:
		for i in range(len(fname)):
			if fname[i] == '.':
				fext = fname[i:]
	return fext


def startextline(text):
	stars1 = '*' * ((80-len(text))//2)
	stars2 = '*' * (80-len(stars1) - len(text))
	print(f"{stars1}{text}{stars2}")

os.system('cls' if os.name == 'nt' else 'clear')  # clearing the screen

print(f"{'*'*80}")
startextline(' MEDIA FILE MANAGER v1.0 ')
startextline(' BY JIM PINCINI ')
print(f"{'*'*80}")

print(f"\nCurrent Folder: {os.getcwd()}")
fol_in = input(f"\nEnter relative path of folder to examine ('.' for current folder): ")
fol_in = fol_in.rstrip('/')
#fol_in = 'podcasts/Under The Skin with Russell Brand'

if fol_in != '.':
	print(f"\nFor Folder: {str(os.getcwd()) + '/' + fol_in + '/'}")
else:
	print(f"\nFor Folder: {str(os.getcwd()) + '/'}")

filelistf = []
filelist = []

print(f"\nAudio File list: ")

for filename in sorted(os.listdir(fol_in), key=str.lower):
	if os.path.isfile(os.path.join(fol_in, filename)):
		try:
			audio = EasyID3(os.path.join(fol_in, filename))
		except:
			pass
		else:
			print(f"{filename}")
			filelist.append(filename)
			filelistf.append(os.path.relpath(os.path.join(fol_in, filename))) # this looks very good!!!!
# the above line looks to return the path relative to where the gehmensch.py script is run!!!
# filelist.append(os.path.abspath(os.path.join(fol_in, filename))) # gives absolute path, not so relevant

if len(filelist) == 0:
	print(f"NO AUDIO FILES FOUND!")
	quit()

for i in range(len(filelistf)):
	filename = filelist[i]
	filenamef = filelistf[i]

	audio = EasyID3(filenamef)

	print(f"\nFile:     {filename}")
	try:
		print(f"Artist:   {str(audio['artist']).strip('[]')}")
	except:
		print(f"Artist:   UNKNOWN!")
		audio['artist'] = 'unknown'
	
	try:
		print(f"Album:    {str(audio['album']).strip('[]')}")
	except:
		print(f"Album:    UNKNOWN!")
		audio['album'] = 'unknown'
	
	try:
		print(f"Title:    {str(audio['title']).strip('[]')}")
	except:
		print(f"Title:    UNKNOWN!")
		audio['title'] = 'unknown'
	
	try:
		print(f"Length:   {int(MP3(filenamef).info.length)} s")
	except:
		print(f"Length:   UNKNOWN!")
	
	audio.save()

	u_in = input(f"\nChange file properties (y/n): ").lower()
	if u_in == 'y':
		u_in_art = input(f"Change Artist (y/n): ").lower()
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
			new_fname = input(f"Enter New Filename (with correct .ext): ")
			while findext(new_fname) != findext(filename):
				print(f"Old file .ext: {findext(filename)}")
				u_in_ext = input(f"Are you sure you want to change the file .ext? (y/n): ").lower()
				if u_in_ext == 'y':
					break
				new_fname = input(f"Enter New Filename (with correct .ext): ")
			os.rename(filenamef, os.path.relpath(fol_in) + '/' + new_fname)
