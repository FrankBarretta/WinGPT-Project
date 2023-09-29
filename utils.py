#_____________________________________________________________________

#utils.py


import openai
import speech_recognition as sr
import pyttsx3
import re

from config import Config

from commands import Commands

openai.api_key = Config.API_KEY
engine = pyttsx3.init()

def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model=Config.MODEL,
        messages=messages,
        max_tokens=Config.MAX_TOKENS,
        temperature=Config.TEMPERATURE
    )
    answer = response.choices[-1].message.content
    return answer

def audio_transcription():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if Config.USER_LANGUAGE == 'it-IT':
            print("Parla adesso...")
        else:
            print("Speak now...")
        audio = recognizer.listen(source)

    try:
        transcribed_text = recognizer.recognize_google(audio, language=Config.USER_LANGUAGE)
        return transcribed_text
    except sr.UnknownValueError:
        if Config.USER_LANGUAGE == 'it-IT':
            print("Non ho capito.")
        else:
            print("I didn't understand.")
        return ""
    except sr.RequestError:
        if Config.USER_LANGUAGE == 'it-IT':
            print("Impossibile completare la richiesta.")
        else:
            print("Unable to complete the request.")
        return ""

import re

def speak(text):
    if Config.VOICE_FOR_GPT:
        exclude_phrases = [
            Commands.AI_LAUNCH_PROGRAM_PATH, Commands.AI_GO_TO_PATH_DIRECTORY,
            Commands.AI_CREATE_FILE_COMMAND, Commands.AI_CREATE_FILE_WITH_CONTENT_COMMAND,
            Commands.AI_CREATE_DIR_PATH, Commands.AI_LAUNCH_STEAM_STORE,
            Commands.AI_LAUNCH_STEAM_LIBRARY
        ]

        filtered_text = text
        for phrase in exclude_phrases:
            # Ensure commands are valid regular expressions
            phrase = re.escape(phrase)
            # Match command followed by optional whitespace, newline or "--" and quoted text
            regex_pattern = f"{phrase}((\s|\n|--)*\".*?\")*"
            filtered_text = re.sub(regex_pattern, "", filtered_text, flags=re.DOTALL)

        # Remove multiple whitespace
        filtered_text = re.sub(r'\s+', ' ', filtered_text)

        if filtered_text.strip():
            engine.say(filtered_text)
            engine.runAndWait()


