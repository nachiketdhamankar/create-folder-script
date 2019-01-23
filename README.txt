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