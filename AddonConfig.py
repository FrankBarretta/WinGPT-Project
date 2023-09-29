#_____________________________________________________________________

#AddonConfig.py

import getpass


class Config:
    # User's language
    USER_LANGUAGE = 'it-IT'

    # AI Assistant's name
    AI_ASSISTANT_NAME = "WinGPT"

    # Name of the PC's user
    PC_NAME = getpass.getuser()

    # Operating system
    OPERATING_SYSTEM = "Windows"
