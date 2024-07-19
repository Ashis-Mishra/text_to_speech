from gtts import gTTS
import os

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")

text = "Hello, Myself Alex Smith, first year engineering student at Tech University. I am currently serving as the President of Student Relations. I am in the Information Technology branch, focusing on the field of Artificial Intelligence and Machine Learning, particularly in Neural Networks. I recently won the National Innovation Hackathon. Thanks for listening to this sample audio!"
filename = "file.mp3"

text_to_speech(text, filename)
