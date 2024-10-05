# import pysrt
# from googletrans import Translator

# def translate_srt(input_srt_file, output_srt_file, target_language='ar'):
#     # Initialize the Google Translate API
#     translator = Translator()
    
#     # Load the .srt file
#     subs = pysrt.open(input_srt_file)

#     # Loop through each subtitle
#     for sub in subs:
#         # Translate the text to Arabic
#         translated = translator.translate(sub.text, dest=target_language)
#         sub.text = translated.text  # Update the subtitle text with the translation
    
#     subs.save(output_srt_file, encoding='utf-8')

# # Example usage
# input_srt = '01_gradient-descenten.srt'    # Path to your original English .srt file


# output_srt = 'arabic.srt'  # Path to save the translated Arabic .srt file

# translate_srt(input_srt, output_srt, target_language='ar')
from google.cloud import translate_v2 as translate
import pysrt

def translate_srt(input_srt_file, output_srt_file, target_language='ar'):
    translate_client = translate.Client()

    subs = pysrt.open(input_srt_file)
    for sub in subs:
        result = translate_client.translate(sub.text, target_language=target_language)
        sub.text = result['translatedText']
    
    subs.save(output_srt_file, encoding='utf-8')

# Example usage
input_srt = '01_gradient-descenten.srt'  # مسار ملف الترجمة الأصلي
output_srt = 'arabic.srt'  # مسار الملف المترجم
translate_srt(input_srt, output_srt, target_language='ar')  # ترجمة للعربية
#NKHUHUH