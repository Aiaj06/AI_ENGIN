import speech_recognition as sr
from googletrans import Translator
from spellchecker import SpellChecker
from language_tool_python import LanguageTool
from PyPDF2 import PdfReader
import cv2
import pytesseract
from fpdf import FPDF
from gtts import gTTS
from io import BytesIO
from googletrans import Translator
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from docx import Document
import textwrap


class Grammar_checker:
    @staticmethod
    def extract_text_from_image(scanned_image):
        gray_image = cv2.cvtColor(scanned_image, cv2.COLOR_RGB2GRAY)
        text = pytesseract.image_to_string(gray_image)
        print("Extracted Text from Image:")
        print(text)
        return text
    @staticmethod
    def extract_text_from_pdf(pdf_path):
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            print("Extracted Text from PDF:")
            print(text)
            return text
    @staticmethod
    def extract_text_from_text_file(text_file_path):
        with open(text_file_path, 'r') as file:
            text = file.read()
            print("Text from Text File:")
            print(text)
            return text
    @staticmethod
    def extract_text_from_word_document(docx_path):
        doc = Document(docx_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
        print("Text from Word Document:")
        print(text)
        return text
    @staticmethod
    def correct_spelling_and_grammar(text):
        spell = SpellChecker()
        tool = LanguageTool('en-US')

        # Correct spelling
        words = text.split()
        corrected_words = [spell.correction(word) for word in words if spell.correction(word) is not None]
        corrected_text = ' '.join(corrected_words)

        # Grammar check
        matches = tool.check(corrected_text)
        if matches:
            for match in matches:
                suggested_word = match.replacements[0] if match.replacements else "<no suggestions>"
                start = match.offset
                end = match.offset + match.errorLength
                corrected_text = corrected_text[:start] + suggested_word + corrected_text[end:]

        return corrected_text
if __name__=="__main__" :
    grammar_checker=Grammar_checker()
    text="summarized_text.pdf"
    gt=grammar_checker.extract_text_from_pdf(text)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    ct=grammar_checker.correct_spelling_and_grammar(gt)
    print(ct)
