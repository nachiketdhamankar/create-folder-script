"""
Creates folders in the current working directory.

Arguments:
    Mandatory:
        name_of_folder (string) : Suffix for each folder name.
        number_of_folders (int) : The number of folders created.

    Optional:
        -path (string) : Path inside which folders are to be created(to be entered in double quotes).

Syntax:
    $ python createFolders.py {folder_name} {number_of_folders}
    or
    $ python createFolders.py {folder_name} {number_of_folders} -p "{path in double quotes}"

Result:
    Creates folders with the following format:

        name_of_folder 1
        name_of_folder 2
        .. and so on.
"""
import os
import argparse
from utils.utils import logger
import logging
import pathlib

def createFolders(number_of_folders, name_of_folder, path):
    try:
        for lecture_number in range(int(number_of_folders)):
            os.mkdir(path + "/" + name_of_folder+ " " + str(lecture_number+1))
            if logger.isEnabledFor(logging.INFO):
                logger.debug("%s_%s is created in %s" %(name_of_folder , str(lecture_number+1), str(path)))
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)


parser = argparse.ArgumentParser(description = __doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('name_of_folder', help = 'Name of each folder to be created')
parser.add_argument('number_of_folders', help = 'Number of folders to be created')
parser.add_argument('-path', help = 'Enter the path of the folder in which the folders are to be created in double quotes')
args = parser.parse_args()


if args.path is None:
    createFolders(args.number_of_folders, args.name_of_folder, os.getcwd())
else:
    createFolders(args.number_of_folders, args.name_of_folder, args.path)
