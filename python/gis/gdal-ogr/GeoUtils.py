"""
Class: Utility functions for GIS scripts
Author: Colin Stief

"""
import os

def horde_files(directory, file_types):
    """
    Create a dictionary of files of a specific type from a directory
    Each entry is a key value pair of the filename and the complete path
    """

    ## Create an empty dictionary
    file_list = {}

    ## Loop through given directory and grab all the files with the given extensions
    for root, dirs, files in os.walk(directory):
        for name in files:
            
            ## Set to lowercase 
            name = name.lower()

            ## Check if the extension matches one of the extensions provided
            if any(name[name.rfind("."):len(name)][1:] in file_type for file_type in file_types):

                ## Strip the last part
                raw_name = name[:name.rfind(".")]

                ## Remove weird characters from name and set to lowercase
                clean_name = ''.join(char for char in raw_name if char.isalnum()).lower()
                
                ## Get the full path
                full_file_path = os.path.join(root, name)
                file_list[clean_name] = full_file_path

    ## Return the completed dictionary
    return file_list
