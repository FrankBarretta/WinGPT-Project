#_____________________________________________________________________

#.\addons\create_file.py

import subprocess
import re
import os

from commands import Commands
from AddonConfig import Config

class FileManager:
    @staticmethod
    def create_file(create_file_func, create_file_content_func):
        try:
            file_path = os.path.dirname(create_file_func)
            os.makedirs(file_path, exist_ok=True)

            with open(create_file_func, "w") as file:
                if create_file_content_func:
                    file.write(create_file_content_func)

            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Creazione del file: {create_file_func}")
            else:
                print(f"Creating file: {create_file_func}")
        except (FileNotFoundError, PermissionError) as e:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Errore durante la creazione del file: {create_file_func}: {str(e)}")
            else:
                print(f"Error while creating file: {create_file_func}: {str(e)}")

    @staticmethod
    def extract_create_file_func(create_file_command):
        match_create_file = re.search(Commands.AI_CREATE_FILE_COMMAND + r'"(.*?)"[,.;]?', create_file_command)
        if match_create_file:
            create_file_func = match_create_file.group(1)
            return create_file_func
        return None

    @staticmethod
    def extract_create_file_content_func(create_file_content_command):
        match_create_file_content = re.search(Commands.AI_CREATE_FILE_WITH_CONTENT_COMMAND + r'"(.*?)"[,.;]?', create_file_content_command)
        if match_create_file_content:
            create_file_content_func = match_create_file_content.group(1)
            return create_file_content_func
        return ""

    @staticmethod
    def create_file_real_command(create_file_command):
        create_file_commands = re.findall(
            r'--create_file_"([^"]*)"(?:\s*--)?\s*--create_file_content_"(.*?)"(?=\W|$)',
            create_file_command,
            re.DOTALL
        )


        for create_file_func, create_file_content_func in create_file_commands:
            FileManager.create_file(create_file_func, create_file_content_func)
