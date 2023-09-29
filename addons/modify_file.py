#_____________________________________________________________________

#.\addons\modify_file.py

import os
import re

from commands import Commands
from AddonConfig import Config

class ModifyFileManager:
    def __init__(self):
        self.modifying_file = False
        self.file_to_modify = None

    def modify_file(self, file_path, new_content):
        try:
            with open(file_path, "w") as file:
                file.write(new_content)

            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Modifica del file: {file_path}")
            else:
                print(f"Modifying file: {file_path}")
        except (FileNotFoundError, PermissionError) as e:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Errore durante la modifica del file: {file_path}: {str(e)}")
            else:
                print(f"Error while modifying file: {file_path}: {str(e)}")

    def extract_file_path(self, modify_file_command):
        match_modify_file = re.search(Commands.AI_MODIFY_FILE_COMMAND + r'"(.*?)"[,.;]?', modify_file_command)
        if match_modify_file:
            file_path = match_modify_file.group(1)
            return file_path
        return None

    def extract_new_content(self, modify_file_command):
        match_new_content = re.search(Commands.AI_MODIFIED_FILE_CONTENT_COMMAND + r'"(.*?)"[,.;]?', modify_file_command)
        if match_new_content:
            new_content = match_new_content.group(1)
            return new_content
        return ""

    def modify_file_real_command(self, modify_file_command, messages):
        if self.modifying_file:
            # We expect the assistant's response to be the new file content
            new_content = self.extract_new_content(modify_file_command)
            if new_content:
                self.modify_file(self.file_to_modify, new_content)
                self.modifying_file = False
                self.file_to_modify = None
        else:
            file_path = self.extract_file_path(modify_file_command)
            if file_path:
                self.send_file_content_for_modification(file_path, messages)
                self.modifying_file = True
                self.file_to_modify = file_path

    def send_file_content_for_modification(self, file_path, messages):
        try:
            with open(file_path, "r") as file:
                content = file.read()

            # Automatically send a message with the file content to GPT-3
            if Config.USER_LANGUAGE == 'it-IT':
                messages.append({
                    'role': 'user',
                    'content': f"Questo è il contenuto del file che devi modificare:\n\n{content}\n\nScrivi il nuovo contenuto del file in questo modo: --modified_file_content_\"nuovo contenuto\"."
                })
            else:
                messages.append({
                    'role': 'user',
                    'content': f"This is the content of the file you need to modify:\n\n{content}\n\nWrite the new content of the file in this way: --modified_file_content_\"new content\"."
                })
        except (FileNotFoundError, PermissionError) as e:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Errore durante la lettura del file: {file_path}: {str(e)}")
            else:
                print(f"Error while reading file: {file_path}: {str(e)}")