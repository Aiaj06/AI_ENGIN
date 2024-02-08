# AI-ENGINE

TextProcessor 
The TextProcessor class provides methods for extracting text from different sources, summarization, and text analysis.

Methods
extract_text_from_image(scanned_image): Extracts text from a scanned image using OCR.
extract_text_from_pdf(pdf_path): Reads a PDF file and extracts text from each page.
extract_text_from_text_file(text_file_path): Reads a text file and returns the content.
extract_text_from_word_document(docx_path): Reads a Word document and returns the text.
get_sentences_count(text, summary_length): Calculates the number of sentences for summarization.
summarize_text_sumy(text, sentences_count): Uses LSA for text summarization.
text_to_pdf(text, filename="summarized_text.pdf"): Converts text to a PDF file with specified formatting.
text_in_words_and_sentences(text): Counts the number of words and sentences in the text.
extracted_text_words(text, num_keywords=5): Extracts keywords using TF-IDF.
summarize_content(text, selected_keywords): Extracts sentences containing selected keywords and generates a summary.
calculate_reduction_percentages(...): Calculates reduction in words and sentences.
create_bullet_points(text, format_choice): Processes text using spaCy and creates bullet points or paragraphs.

Dictation 
The Dictation class provides methods for correcting spelling and grammar, translating text, and recognizing speech.

Methods
correct_spelling_and_grammar(text): Corrects spelling and grammar using SpellChecker and LanguageTool.
translate_text(text, target_language='en'): Translates text to the specified target language using Google Translate API.
recognize_and_correct(): Recognizes speech, translates to English, and corrects spelling and grammar.

Translation_File 
The Translation_File class provides methods for extracting text from different sources and translating it.

Methods
extract_text_from_image(scanned_image): Extracts text from a scanned image using OCR.
extract_text_from_pdf(pdf_path): Reads a PDF file and extracts text from each page.
extract_text_from_text_file(text_file_path): Reads a text file and returns the content.
extract_text_from_word_document(docx_path): Reads a Word document and returns the text.
translate_text(text, target_language): Translates text using Google Translate API.
text_to_pdf(text, filename="summarized_text.pdf"): Converts text to a PDF file using FPDF.

Audioprocess 
The Audioprocess class provides methods for extracting text from different sources and converting it to speech.

Methods
extract_text_from_image(scanned_image): Extracts text from a scanned image using OpenCV and Tesseract.
extract_text_from_pdf(pdf_path): Reads a PDF file and extracts text from each page using PyPDF2.
extract_text_from_text_file(text_file_path): Reads a text file and returns its content.
extract_text_from_word_document(docx_path): Reads a Word document and returns the text.
text_to_speech(text, language): Converts text to speech using gTTS.
detect_language(text): Detects the language of the given text.

Usage

Install the required libraries (pip install -r requirements.txt).
Import the necessary classes in your script.
Instantiate the classes and use their methods as needed.
Example Usage


Notes
Ensure the necessary libraries are installed.
Refer to the method documentation for detailed usage instructions.
Customize the code according to your specific requirements.
