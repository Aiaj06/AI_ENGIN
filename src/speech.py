# Importing necessary libraries
import speech_recognition as sr
from spellchecker import SpellChecker
from language_tool_python import LanguageTool
from googletrans import Translator
import time

# Class for handling dictation tasks
class Dictation:
    @staticmethod
    def correct_spelling_and_grammar(text):
        # Spell checking using SpellChecker
        spell = SpellChecker()
        # Grammar checking using LanguageTool
        tool = LanguageTool('en-US')

        # Correcting spelling
        corrected_words = [spell.correction(word) for word in text.split() if spell.correction(word) is not None]
        corrected_text = ' '.join(corrected_words)

        # Correcting grammar
        matches = tool.check(corrected_text)
        for match in matches:
            suggested_word = match.replacements[0] if match.replacements else "<no suggestions>"
            start, end = match.offset, match.offset + match.errorLength
            corrected_text = corrected_text[:start] + suggested_word + corrected_text[end:]

        return corrected_text

    @staticmethod
    def translate_text(text, target_language='en'):
        # Translation using Googletrans
        translator = Translator()

        if not text:
            print("Error: Empty text provided for translation.")
            return ""

        print("Text before translation:", text)

        try:
            # Performing translation
            translation = translator.translate(text, dest=target_language)
            translated_text = translation.text
            print("Translated Text:", translated_text)
            return translated_text
        except Exception as e:
            print(f"Error during translation: {e}")
            return ""

    @staticmethod
    def recognize_and_correct():
        # Speech recognition using SpeechRecognition
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak something...")

            try:
                # Adjusting for ambient noise
                recognizer.adjust_for_ambient_noise(source)
                # Listening to user's speech
                audio = recognizer.listen(source, timeout=20)
                # Recognizing and printing original text
                user_input = recognizer.recognize_google(audio, language='auto')
                print(f"Original Text: {user_input}")

                # Translating and correcting speech
                translated_text = Dictation.translate_text(user_input, target_language='en')
                corrected_text = Dictation.correct_spelling_and_grammar(translated_text)
                return corrected_text

            except sr.UnknownValueError:
                print("No speech detected.")
                return ""
            except sr.RequestError as e:
                print(f"Error making the request to Google Speech Recognition service: {e}")
                return ""
            except Exception as e:
                print(f"Error: {e}")
                return ""

# Main function
def main():
    # Prompting the user to choose between text or speech input
    user_option = input("Select 'text' or 'speech': ")

    if user_option == "speech":
        # If speech input is chosen
        start_time = time.time()
        text = Dictation.recognize_and_correct()
        end_time = time.time()
        print(f"Corrected Text: {text}")
        print(f"Execution Time: {end_time - start_time} seconds")
    elif user_option == "text":
        # If text input is chosen
        text_input = input("Enter text: ")
        start_time = time.time()
        corrected_text = Dictation.correct_spelling_and_grammar(text_input)
        end_time = time.time()
        print(f"Corrected Text: {corrected_text}")
        print(f"Execution Time: {end_time - start_time} seconds")
    else:
        print("Choose the correct option.")

# Entry point of the script
if __name__ == "__main__":
    main()
