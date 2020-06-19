'''

This script constructs an .M3U playlist file
You may wish to first run mediamensch.py over the audio files you want to add
to the playlist to ensure the relevant information is included in the .M3U
files.

playmensch will add all files (not folders) to the playlist if they have a
suitable extension.

playmensch should be run from where the .m3u files are needed


#EXTM3U

#EXTINF:105, Example artist - Example title
C:\Files\My Music\Example.mp3

#EXTINF:321, Example Artist2 - Example title2
C:\Files\My Music\Favorites\Example2.ogg

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

# files with these extensions will be added to the playlist:
# exts = ['.mp3']

os.system('cls' if os.name == 'nt' else 'clear')  # clearing the screen

print(f"{'*'*80}")
startextline(' .M3U PLAYLIST GENERATOR v1.0 ')
startextline(' BY JIM PINCINI ')
print(f"{'*'*80}")

print(f"\nCurrent Folder: {os.getcwd()}")
fol_in = input(f"\nEnter relative path of folder containing files to add to playlist ('.' for current folder):\n ")
fol_in = fol_in.rstrip('/')
#fol_in = 'podcasts/Under The Skin with Russell Brand'

if fol_in != '.':
	print(f"\nFor Folder: {str(os.getcwd()) + '/' + fol_in + '/'}")
else:
	print(f"\nFor Folder: {str(os.getcwd()) + '/'}")

filelistf = []
filelist = []

for filename in sorted(os.listdir(fol_in), key=str.lower):
	if os.path.isfile(os.path.join(fol_in, filename)):  #and findext(filename).lower() in exts:
		try:
			audio = EasyID3(os.path.join(fol_in, filename))
		except:
			print(f"### NOT VALID: {filename}")
		else:
			filelist.append(filename)
			filelistf.append(os.path.relpath(os.path.join(fol_in, filename)))

if len(filelistf) == 0:
	print(f"NO AUDIO FILES FOUND!")
	quit()

print(f"\nAudio File list: ")
for filename in filelist:
	print(f"{filename}")

plist = input(f"\nWhat is the playlist name?: ")
if plist.lower().endswith('.m3u'):
	plist = plist[:-4]
plistf = plist + '.m3u'

with open(plistf, 'w') as fout:
	fout.write(f"#EXTM3U\n\n")

	for i in range(len(filelistf)):
		filenamef = filelistf[i]
		audio = EasyID3(filenamef)
		artist = str(audio['artist']).strip('[]').strip('\'')
		title = str(audio['title']).strip('[]').strip('\'')
		try:
			length = int(MP3(filenamef).info.length)
		except:
			length = -1
		finally:
			fout.write(f"#EXTINF:{length}, {artist} - {title}")
			fout.write(f"\n{filenamef}\n\n")

print(f"\nPlaylist filename: {plistf}\n")
