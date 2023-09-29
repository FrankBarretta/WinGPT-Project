#_____________________________________________________________________

#.\addons\execute_program_as_admin.py

import subprocess
import re
import ctypes

from commands import Commands
from AddonConfig import Config

class AdminProgramManager:
    @staticmethod
    def execute_program_as_admin(program_as_admin_name, program_as_admin_path=None):
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                subprocess.Popen(program_as_admin_name)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", program_as_admin_name, None, None, 1)

            AdminProgramManager.print_message('execution', program_as_admin_name)
        except (FileNotFoundError, PermissionError) as e:
            AdminProgramManager.print_message('error', program_as_admin_name, str(e))

            if program_as_admin_path:
                try:
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        subprocess.Popen(program_as_admin_path)
                    else:
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", program_as_admin_path, None, None, 1)

                    AdminProgramManager.print_message('execution', program_as_admin_path)
                except (FileNotFoundError, PermissionError) as e:
                    AdminProgramManager.print_message('error', program_as_admin_path, str(e))

    @staticmethod
    def print_message(message_type, program, error=None):
        messages = {
            'execution': {
                'it-IT': f"Esecuzione del programma come amministratore: {program}",
                'default': f"Executing program as admin: {program}"
            },
            'error': {
                'it-IT': f"Errore durante l'esecuzione del programma come amministratore: {program}: {error}",
                'default': f"Error while executing program as admin: {program}: {error}"
            }
        }

        print(messages[message_type]['it-IT'] if Config.USER_LANGUAGE == 'it-IT' else messages[message_type]['default'])

    @staticmethod
    def extract_program_as_admin_name(execute_program_as_admin_command):
        match = re.search(Commands.AI_LAUNCH_PROGRAM_AS_ADMIN_NAME + r'"(.*?)"[,.;]?', execute_program_as_admin_command)
        return match.group(1) if match else None

    @staticmethod
    def extract_program_as_admin_path(execute_program_as_admin_command_path):
        match_path = re.search(Commands.AI_LAUNCH_PROGRAM_AS_ADMIN_PATH + r'"(.*?)"[,.;]?', execute_program_as_admin_command_path)
        return match_path.group(1) if match_path else None

    @staticmethod
    def execute_program_as_admin_command(execute_program_as_admin_command):
        program_as_admin_name = AdminProgramManager.extract_program_as_admin_name(execute_program_as_admin_command)
        program_as_admin_path = AdminProgramManager.extract_program_as_admin_path(execute_program_as_admin_command)

        if program_as_admin_name:
            try:
                AdminProgramManager.execute_program_as_admin(program_as_admin_name, program_as_admin_path)
            except (FileNotFoundError, PermissionError):
                if program_as_admin_path:
                    AdminProgramManager.execute_program_as_admin(program_as_admin_path, None)
                else:
                    print(f"Program path not found for execute_program_as_admin_command: {execute_program_as_admin_command}")
            return

        if program_as_admin_path:
            try:
                AdminProgramManager.execute_program_as_admin(program_as_admin_path, None)
            except (FileNotFoundError, PermissionError):
                pass
