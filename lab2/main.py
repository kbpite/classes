"""
FILESYSTEM SNAPSHOT GENERATOR v0.2

* script generates a snapshot of files and directories for a given location in the filesystem
* location is obtained from the user
* location is validated (whether it exists or not)
* output of the script is saved in a text file named $TIMESTAMP in /snapshots folder
"""

from time import time
from os import listdir, makedirs
from os.path import isdir, join, basename, normpath, exists

PREFIX = '   '


def list_dir(folder, parents=0):
	result = parents*PREFIX + folder + '\n'
	parents += 1
	for file_ in listdir(folder):
		file_path = join(folder, file_)
		if isdir(file_path):
			result += list_dir(file_path, parents)
		else:
			result += parents*PREFIX + file_path + '\n'
	return result


def main():
	target = raw_input('Please provide path to a folder and press ENTER\n')
	if isdir(target):
		if not exists('snapshots'):
			makedirs('snapshots')
		outname = 'snapshots/' + str(int(time())) + '.txt'
		with open(outname, 'w') as outfile:
			outfile.write(list_dir(target))
	else:
		print '[ERROR] Given path is not a directory'


if __name__ == "__main__":
	main()

