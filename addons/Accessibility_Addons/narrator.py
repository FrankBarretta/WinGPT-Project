#_____________________________________________________________________

#.\addons\Accessibility_Addons\narrator.py

import subprocess
import re
import pyautogui

from commands import Commands
from AddonConfig import Config

class NarratorManager:
    @staticmethod
    def launch_narrator(launch_narrator_key):
        try:
            pyautogui.keyDown('win')
            pyautogui.keyDown('ctrl')
            pyautogui.press('enter')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('win')

            NarratorManager.print_message('execution', launch_narrator_key)
        except pyautogui.FailSafeException as e:
            NarratorManager.print_message('error', launch_narrator_key, str(e))

    @staticmethod
    def print_message(message_type, key, error=None):
        messages = {
            'execution': {
                'it-IT': f"Simulazione di Windows+Ctrl+Enter: {key}",
                'default': f"Simulating Windows+Ctrl+Enter: {key}"
            },
            'error': {
                'it-IT': f"Errore durante la simulazione di Windows+Ctrl+Enter per l'avvio del Narratore Windows: {key}: {error}",
                'default': f"Error while simulating Windows+Ctrl+Enter to launch Windows Narrator: {key}: {error}"
            }
        }

        print(messages[message_type]['it-IT'] if Config.USER_LANGUAGE == 'it-IT' else messages[message_type]['default'])

    @staticmethod
    def extract_launch_narrator(launch_narrator_command):
        launch_narrator_keys = re.findall(Commands.AI_LAUNCH_NARRATOR_COMMAND, launch_narrator_command)
        return launch_narrator_keys

    @staticmethod
    def launch_narrator_command(launch_narrator_command):
        launch_narrator_keys = NarratorManager.extract_launch_narrator(launch_narrator_command)

        for launch_narrator_key in launch_narrator_keys:
            NarratorManager.launch_narrator(launch_narrator_key)
