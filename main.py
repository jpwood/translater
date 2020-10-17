from googletrans import Translator
import os
import pandas as pd

LANGUAGES = {
    'ar': 'arabic',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'ja': 'japanese',
    'ko': 'korean',
    'pa': 'punjabi',
    'ru': 'russian',
    'tr': 'turkish'
}

def removesuffix(self: str, suffix: str, /) -> str:
    return self[:-len(suffix)]

def translate_all_wavs(path: str):
    os.chdir(path)
    original_wav_names = [filename for filename in os.listdir() if filename.endswith(".wav")]
    names_to_translate = [removesuffix(name, ".wav") for name in original_wav_names]
    translator = Translator(service_urls=['translate.google.com'])
    translated = dict()
    for name in names_to_translate:
        translated[name] = {language: translator.translate(name, dest=language_key).text for language_key, language in LANGUAGES.items()}
    output_file_name = path.split("/")[-1]
    pd.DataFrame.from_dict(translated, orient='index').to_csv(f'{output_file_name}.csv')

translate_all_wavs("C:/Users/jonwo/Desktop/exports")