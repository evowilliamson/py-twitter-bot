from pathlib import Path
import os
import shutil

""" Module that contains function pertaining to path management """

def create_dir_in_user_home(dir, overwrite=True):
    """ Creates a directory in the home directory

    Args:
        dir(str): The directory to create
        overwrite(bool): true: removes the existing directory, false: don't try to remove
    
    """

    if overwrite:
        clean_dir_in_user_home(dir)
    os.mkdir(Path(get_user_home(), dir))


def clean_dir_in_user_home(dir):
    """ Cleans a directory in the home directory

    Args:
        dir(str): The directory to create
    
    """
        
    if Path(str(get_user_home()), dir).exists() and Path(str(get_user_home()), dir).is_dir():
        shutil.rmtree(Path(get_user_home(), dir))


def get_dir_in_user_home(dir):
    """ Gets a directory in the home directory

    Args:
        dir(str): The directory to get    

    """

    return str(Path(get_user_home(), dir))

def get_user_home():
    """ Gets the home directory 
    """

    return str(Path.home())