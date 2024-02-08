import speech_recognition as sr
from spellchecker import SpellChecker
from language_tool_python import LanguageTool
from googletrans import Translator
import time

class Dictation:
    @staticmethod
    def correct_spelling_and_grammar(text):
        spell = SpellChecker()
        tool = LanguageTool('en-US')

        corrected_words = [spell.correction(word) for word in text.split() if spell.correction(word) is not None]
        corrected_text = ' '.join(corrected_words)

        matches = tool.check(corrected_text)
        for match in matches:
            suggested_word = match.replacements[0] if match.replacements else "<no suggestions>"
            start, end = match.offset, match.offset + match.errorLength
            corrected_text = corrected_text[:start] + suggested_word + corrected_text[end:]

        return corrected_text

    @staticmethod
    def translate_text(text, target_language='en'):
        translator = Translator()

        if not text:
            print("Error: Empty text provided for translation.")
            return ""

        print("Text before translation:", text)

        try:
            translation = translator.translate(text, dest=target_language)
            translated_text = translation.text
            print("Translated Text:", translated_text)
            return translated_text
        except Exception as e:
            print(f"Error during translation: {e}")
            return ""

    @staticmethod
    def recognize_and_correct():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak something...")

            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=20)
                user_input = recognizer.recognize_google(audio, language='auto')
                print(f"Original Text: {user_input}")

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

def main():
    user_option = input("Select 'text' or 'speech': ")

    if user_option == "speech":
        start_time = time.time()
        text = Dictation.recognize_and_correct()
        end_time = time.time()
        print(f"Corrected Text: {text}")
        print(f"Execution Time: {end_time - start_time} seconds")
    elif user_option == "text":
        text_input = input("Enter text: ")
        start_time = time.time()
        corrected_text = Dictation.correct_spelling_and_grammar(text_input)
        end_time = time.time()
        print(f"Corrected Text: {corrected_text}")
        print(f"Execution Time: {end_time - start_time} seconds")
    else:
        print("Choose the correct option.")

if __name__ == "__main__":
    main()