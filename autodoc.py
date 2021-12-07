import os
import sys
import fitz 
import deepl 
import config
import pathlib


"""
target_language codes (basic):

"BG" - Bulgarian
"CS" - Czech
"DA" - Danish
"DE" - German
"EL" - Greek
"EN" - English
"ES" - Spanish
"ET" - Estonian
"FI" - Finnish
"FR" - French
"HU" - Hungarian
"IT" - Italian
"JA" - Japanese
"LT" - Lithuanian
"LV" - Latvian
"NL" - Dutch
"PL" - Polish
"PT" - Portuguese (all Portuguese varieties mixed)
"RO" - Romanian
"RU" - Russian
"SK" - Slovak
"SL" - Slovenian
"SV" - Swedish
"ZH" - Chinese

target_language codes (specific):

"EN-GB" - English (British)
"EN-US" - English (American)
"PT-PT" - Portuguese 
"PT-BR" - Portuguese (Brazilian)

"""

def main():
    pdf_file = os.path.join(pathlib.Path(__file__).resolve().parent, "files", "sample.pdf")
    translator = deepl.Translator(config.auth_key) 
    target_language = "FR"

    fin_translation = ""
    with fitz.open(pdf_file) as doc:
        text = ""
        for page in doc:
            text = page.get_text()
            result = translator.translate_text(text, target_lang=target_language) 
            translation = result.text
            fin_translation = fin_translation + translation

    txt_file = os.path.join(pathlib.Path(__file__).resolve().parent, "files", "sample.txt")
    with open(txt_file, "w") as f:
        f.write(fin_translation)
            

if __name__ == "__main__":
    main()
