#_____________________________________________________________________

#config.py

import socket
import getpass

from PROMPT import Prompt

class Config:
    # PC System Settings
    PC_NAME = getpass.getuser()
    OPERATING_SYSTEM = "Windows"

    # Personal Info
    USER_LANGUAGE = 'it-IT'
    USER_NAME = PC_NAME
    AI_ASSISTANT_NAME = "WinGPT"

    # ChatGPT Settings
    API_KEY = ''
    MODEL = 'gpt-3.5-turbo'
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7

    # Vocal Chat Settings
    ENABLE_VOICE_AND_VOCAL = True
    VOICE_FOR_GPT = True
    VOICE_FOR_USER = True
    LISTENING_VOCAL_ALWAYS = False
    LISTENING_VOCAL_KEY_PRESS = True
    LISTENING_VOCAL_KEY_HOLD = False
    VOCAL_ACTIVATION_KEY = 'ctrl'

    # Addons Settings
    ENABLE_ADDONS = True
    ENABLE_EXECUTE_PROGRAM = True
    ENABLE_EXECUTE_PROGRAM_AS_ADMIN = True
    ENABLE_GO_TO_PATH_DIRECTORY = True
    ENABLE_CREATE_FILE = True
#    ENABLE_MODIFY_FILE = True
    ENABLE_CREATE_DIRECTORY = True
    ENABLE_LAUNCH_NARRATOR = True
#    ENABLE_GO_TO_STEAM_LIBRARY = True
#    ENABLE_GO_TO_STEAM_STORE = True

    SYSTEM = Prompt.BASE_PROMPT

    def __init__(self):
        if not self.ENABLE_ADDONS:
            self.disable_all_addons()

        if self.ENABLE_ADDONS:
            Config.SYSTEM += Prompt.AI_RULES_PROMPT

        if self.ENABLE_EXECUTE_PROGRAM:
            Config.SYSTEM += Prompt.AI_LAUNCH_PROGRAM_PROMPT

        if self.ENABLE_GO_TO_PATH_DIRECTORY:
            Config.SYSTEM += Prompt.AI_GO_TO_PATH_PROMPT

        if self.ENABLE_CREATE_FILE:
            Config.SYSTEM += Prompt.AI_CREATE_FILE

        if self.ENABLE_CREATE_DIRECTORY:
            Config.SYSTEM += Prompt.AI_CREATE_DIR

#        if self.ENABLE_MODIFY_FILE:
#            Config.SYSTEM += Prompt.AI_MODIFY_FILE

        if self.ENABLE_LAUNCH_NARRATOR:
            Config.SYSTEM += Prompt.AI_LAUNCH_NARRATOR

        if self.ENABLE_EXECUTE_PROGRAM_AS_ADMIN:
            Config.SYSTEM += Prompt.AI_LAUNCH_PROGRAM_AS_ADMIN_PROMPT

#        if self.ENABLE_GO_TO_STEAM_LIBRARY:
#            Config.SYSTEM += Prompt.AI_LAUNCH_STEAM_LIBRARY_PROMPT

#        if self.ENABLE_GO_TO_STEAM_STORE:
#            Config.SYSTEM += Prompt.AI_LAUNCH_STEAM_STORE_PROMPT

        if self.ENABLE_ADDONS:
            Config.SYSTEM += Prompt.AI_RULES_END

        if not self.ENABLE_VOICE_AND_VOCAL:
            Config.VOICE_FOR_GPT = False
            Config.LISTENING_VOCAL_ALWAYS = False
            Config.LISTENING_VOCAL_KEY_PRESS = False
            Config.LISTENING_VOCAL_KEY_HOLD = False

        if not self.VOICE_FOR_USER:
            Config.LISTENING_VOCAL_ALWAYS = False
            Config.LISTENING_VOCAL_KEY_PRESS = False
            Config.LISTENING_VOCAL_KEY_HOLD = False

    def disable_all_addons(self):
        Config.ENABLE_EXECUTE_PROGRAM = False
        Config.ENABLE_EXECUTE_PROGRAM_AS_ADMIN = False
        Config.ENABLE_GO_TO_PATH_DIRECTORY = False
        Config.ENABLE_CREATE_FILE = False
        Config.ENABLE_CREATE_DIRECTORY = False
#        Config.ENABLE_MODIFY_FILE = False
        Config.ENABLE_LAUNCH_NARRATOR = False
#        Config.ENABLE_GO_TO_STEAM_LIBRARY = False
#        Config.ENABLE_GO_TO_STEAM_STORE = False
        Config.AI_RULES_END = False

config = Config()
