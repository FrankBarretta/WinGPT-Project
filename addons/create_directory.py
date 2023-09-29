#_____________________________________________________________________

#.\addons\create_directory.py

import subprocess
import re
import os

from commands import Commands
from AddonConfig import Config

class DirectoryManager:
    @staticmethod
    def create_directory(create_directory_path):
        try:      
            subprocess.run(['mkdir', create_directory_path], shell=True)

            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Creazione della cartella: {create_directory_path}")
            else:
                print(f"Creating directory: {create_directory_path}")
        except (FileNotFoundError, PermissionError) as e:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Errore durante la creazione della cartella: {create_directory_path}: {str(e)}")
            else:
                print(f"Error while creating directory: {create_directory_path}: {str(e)}")

    @staticmethod
    def extract_create_directory_path(create_dir_command):
        match_create_directory_path = re.search(Commands.AI_CREATE_DIR_PATH + r'"(.*?)"[,.;]?', create_dir_command)
        if match_create_directory_path:
            create_directory_path = match_create_directory_path.group(1)
            return create_directory_path
        return None

    @staticmethod
    def create_directory_command(create_dir_command):
        create_directory_commands = re.findall(
            r'--create_dir_path_"([^"]*)"',
            create_dir_command
        )

        for create_directory_path in create_directory_commands:
            DirectoryManager.create_directory(create_directory_path)
