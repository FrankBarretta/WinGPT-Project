#_____________________________________________________________________

#.\addons\execute_program.py

import subprocess
import re

from commands import Commands
from AddonConfig import Config

class ProgramManager:
    @staticmethod
    def execute_program(program_path):
        try:
            subprocess.Popen(program_path)
            ProgramManager.print_message('execution', program_path)
        except (FileNotFoundError, PermissionError) as e:
            ProgramManager.print_message('error', program_path, str(e))

    @staticmethod
    def print_message(message_type, program, error=None):
        messages = {
            'execution': {
                'it-IT': f"Esecuzione del programma: {program}",
                'default': f"Executing program: {program}"
            },
            'error': {
                'it-IT': f"Errore durante l'esecuzione del programma: {program}: {error}",
                'default': f"Error while executing program: {program}: {error}"
            }
        }

        print(messages[message_type]['it-IT'] if Config.USER_LANGUAGE == 'it-IT' else messages[message_type]['default'])

    @staticmethod
    def extract_program_path(command_path):
        match_path = re.search(Commands.AI_LAUNCH_PROGRAM_PATH + r'"(.*?)"[,.;]?', command_path)
        return match_path.group(1) if match_path else None

    @staticmethod
    def execute_program_command(response):
        program_commands = re.findall(
            r'--execute_program_path_"([^"]*)"',
            response
        )

        for program_path in program_commands:
            ProgramManager.execute_program(program_path)
