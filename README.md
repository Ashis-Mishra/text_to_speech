## Text-to-Speech Conversion using gTTS 
# Project Overview 
This project demonstrates how to convert a text string into speech using the Google Text-to-Speech (gTTS) library in Python. The code takes a text input, converts it into an audio file, and then plays that audio file. It's a simple yet powerful way to generate speech from text programmatically.
# Introduction 
The project involves converting text to speech using the Google Text-to-Speech (gTTS) library. The resulting audio is saved as an MP3 file and played using the operating system's default media player.
# Prerequisites 
Before running the code, ensure you have the following libraries installed:
  ->gtts: To install, run pip install gtts
  ->os: This is a built-in Python module, no installation required.
# Code Explanation 
Import Necessary Libraries 
```python
from gtts import gTTS
import os
```
gTTS: This library is used to convert text to speech using Google's Text-to-Speech API.
os: This module provides a way to interact with the operating system, such as saving and playing files.
# Define the text_to_speech Function 
```python
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")
```
## Parameters:
 text: The string of text to be converted to speech.
 filename: The name of the audio file to save the speech.
 Process: 
```python
gTTS(text=text, lang='en')
tts.save(filename)
os.system(f"start {filename}")
## Define the Text and Filename
```python
text = "Hello, Myself Alex Smith, first year engineering student at Tech University. I am currently serving as the President of Student Relations. I am in the Information Technology branch, focusing on the field of Artificial Intelligence and Machine Learning, particularly in Neural Networks. I recently won the National Innovation Hackathon. Thanks for listening to this sample audio!"
filename = "file.mp3"
```
text: The text string that will be converted to speech.
filename: The name of the MP3 file where the speech will be saved.
## Call the text_to_speech Function 
```python
text_to_speech(text, filename)
```
This line calls the function with the specified text and filename, converting the text to speech and playing the audio file. 
Usage
->Ensure the necessary libraries are installed.
->Modify the text and filename variables as needed.
->Run the script to convert the text to speech and play the audio file.
##Conclusion
This project converts a given text into an MP3 file containing the spoken version of the text using the gTTS library and then plays the audio file. It's a straightforward yet effective way to generate speech from text programmatically.

# Feel free to modify the text and experiment with different languages supported by the gTTS library to enhance your application.





 


