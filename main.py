#_____________________________________________________________________

#main.py


import time
import keyboard
from config import Config
from utils import chat_with_gpt, audio_transcription, speak
from addons.execute_program import ProgramManager
from addons.execute_program_as_admin import AdminProgramManager
from addons.explore_path import PathExplorer
#from addons.Steam_Addons.Launch_Steam_Library import go_to_steam_library_command
#from addons.Steam_Addons.Launch_Steam_Store import go_to_steam_store_command
from addons.create_file import FileManager
#from addons.modify_file import ModifyFileManager
from addons.create_directory import DirectoryManager
from addons.Accessibility_Addons.narrator import NarratorManager





# Create a dictionary of available commands
commands = {
    'execute_program': ProgramManager.execute_program_command,
    'execute_program_as_admin': AdminProgramManager.execute_program_as_admin_command,
    'go_to_path_directory': PathExplorer.go_to_path_directory_command,
    #'go_to_steam_library': go_to_steam_library_command,
    #'go_to_steam_store': go_to_steam_store_command,
    'create_file': FileManager.create_file_real_command,
    #'modify_file': ModifyFileManager.modify_file_real_command,
    'create_directory': DirectoryManager.create_directory_command,
    'launch_narrator': NarratorManager.launch_narrator_command
}



messages = [{'role': 'system', 'content': Config.SYSTEM}]
print("PROMPT SYSTEM: " + Config.SYSTEM)


while True:
    if Config.LISTENING_VOCAL_ALWAYS:
        user_input = audio_transcription()
        if user_input:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Tu ({Config.USER_NAME}): {user_input}")
            else:
                print(f"You ({Config.USER_NAME}): {user_input}")
            messages.append({'role': 'user', 'content': user_input})

    elif Config.LISTENING_VOCAL_KEY_PRESS and keyboard.is_pressed(Config.VOCAL_ACTIVATION_KEY):
        user_input = audio_transcription()
        if user_input:
            if Config.USER_LANGUAGE == 'it-IT':
                print(f"Tu ({Config.USER_NAME}): {user_input}")
            else:
                print(f"You ({Config.USER_NAME}): {user_input}")
            messages.append({'role': 'user', 'content': user_input})

    else:
        user_input = input(f"Tu ({Config.USER_NAME}): ")
        if user_input:
            messages.append({'role': 'user', 'content': user_input})

    response = chat_with_gpt(messages)
    print(f"{Config.AI_ASSISTANT_NAME}: {response}\n")
    speak(f"{response}")

    messages.append({'role': 'assistant', 'content': response})

    # Execute enabled commands
    for command_name, command_func in commands.items():
        #if command_name in globals() and globals()[command_name]:  # Check if the command is enabled
            command_func(response)
