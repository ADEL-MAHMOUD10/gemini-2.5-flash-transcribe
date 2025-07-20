# 🎷 Audio Transcription using Gemini 2.5 Flash

This Python script allows you to **transcribe local audio files** (MP3 format) using Google's Gemini 2.5 Flash model via the `google-genai` API.

You can export the transcription in the following formats:

* `.txt` (plain text)
* `.srt` (SubRip Subtitle)
* `.vtt` (Web Video Text Tracks)

---

## 📦 Requirements

* Python 3.12+
* Google Generative AI API key
* `google-genai` library

Install the required library:

```bash
pip install -q -U google-genai
```

---

## 🔑 Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey).
2. Sign in and generate a new API key.
3. Paste your API key into the script:

```python
client = genai.Client(api_key="YOUR_API_KEY_HERE")
```

---

## 📁 Usage

1. Make sure you have an audio file named `local_audio.mp3` in the same directory as the script.
2. Run the script:

```bash
python transcribe.py
```

3. Follow the prompts:

   * Choose output format: `txt`, `srt`, or `vtt`.
   * Enter the output file name (without extension).

4. The script will:

   * Upload the audio to Gemini.
   * Request transcription in the specified format.
   * Save the transcription to a file.
   * Print the first 10 lines of the transcription in the terminal.

---

## 🧠 Features

* Format validation.
* Error handling for generation and file writing.
* Only the **first 10 lines** of the result are printed to keep the terminal clean.
* Transcription is saved to a new file with the correct extension.

---

## 🖥️ Sample Output

```text
Enter format you need[txt,srt,vtt]: srt
Please wait, transcription is in process...
Transcription successful
Enter the output filename (without extension): my_subs
Transcription saved to my_subs

--- First 10 lines for Transcription ---
1
00:00:00,000 --> 00:00:02,000
Hello and welcome!

2
00:00:02,500 --> 00:00:05,000
This is a demo transcription.
...
```

---

## ❗ Notes

* Transcription accuracy depends on the clarity of the audio.
* Google Gemini 2.5 Flash model is optimized for fast generation but may have limits depending on your API plan.

---

## 📄 License

This project is licensed under the MIT License. Feel free to modify and use it.

---

