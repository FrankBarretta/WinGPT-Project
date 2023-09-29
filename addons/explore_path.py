#_____________________________________________________________________

#.\addons\explore_path.py

import subprocess
import re

from commands import Commands
from AddonConfig import Config

class PathExplorer:
    @staticmethod
    def go_to_path_directory(path_directory):
        try:
            subprocess.Popen(['explorer', path_directory], bufsize=0)
            PathExplorer.print_message('open', path_directory)
        except (FileNotFoundError, PermissionError) as e:
            PathExplorer.print_message('error', path_directory, str(e))

    @staticmethod
    def print_message(message_type, path, error=None):
        messages = {
            'open': {
                'it-IT': f"Apertura della cartella: {path}",
                'default': f"Opening directory: {path}"
            },
            'error': {
                'it-IT': f"Errore durante l'apertura della cartella: {path}: {error}",
                'default': f"Error while opening directory: {path}: {error}"
            }
        }

        print(messages[message_type]['it-IT'] if Config.USER_LANGUAGE == 'it-IT' else messages[message_type]['default'])

    @staticmethod
    def extract_path_directories(dir_command):
        path_directories = re.findall(
            r'--go_to_path_"([^"]*)"',
            dir_command
        )
        return path_directories

    @staticmethod
    def go_to_path_directory_command(dir_command):
        path_directories = PathExplorer.extract_path_directories(dir_command)

        for path_directory in path_directories:
            PathExplorer.go_to_path_directory(path_directory)
