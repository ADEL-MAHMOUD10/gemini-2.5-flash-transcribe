from google import genai # pip install -q -U google-genai
from google.genai import types
# from dotenv import load_dotenv
import os , sys

# load_dotenv()
# api_key = os.getenv('apikey')

client = genai.Client(api_key="") # add your api key here , get it form https://aistudio.google.com/apikey
filname = 'local_audio.mp3'

if not os.path.exists(filname):
    print(f"Error: File '{filname}' not found.")
    sys.exit()

file_format = input('Enter format you need[txt,srt,vtt]: ').lower()
if file_format not in ['txt','srt','vtt']:
    print('please enter srt or vtt or txt')
    exit()
with open(filname,'rb') as f:
    content = f.read()

try:
    print('Please wait, transcription is in process...') 
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_text(text=f'transcribe this file in {file_format} format'),
            types.Part.from_bytes(
                data=content,
                mime_type='audio/mpeg',
            )
        ]
    )
    print('Transcription successful')
    output_name = input('Enter the output filename (without extension): ').strip()

    try:
        with open(f"{output_name}.{file_format}", 'w', encoding='utf-8') as f:
            res = str(response.text)
            f.write(res)
        print(f"Transcription saved to {output_name}")

    except Exception as e:
        print(f'Error writing file: {e}')
    
    lines = str(response.text).splitlines()
    print("\n--- First 10 lines for Transcription ---")
    for line in lines[:10]:
        print(line)

except Exception as e:
    print(f'Error during generation: {e}')
    print("Please check your internet connection or API key.")

