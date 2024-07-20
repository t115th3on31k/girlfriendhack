```python
import speech_recognition as sr
from interpretation_engine.nlp_processing import processUserInput
from ui.user_interface import renderUI

# Initialize the recognizer
r = sr.Recognizer()

def listen_for_input():
    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Listening for voice input...")
        # Adjust the recognizer sensitivity to ambient noise and record audio
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            voice_input = r.recognize_google(audio)
            print(f"Interpreting the following input: {voice_input}")
            return voice_input
        except sr.UnknownValueError:
            # Google Speech Recognition could not understand audio
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            # Could not request results from Google Speech Recognition service
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def voice_command_handler():
    voice_input = listen_for_input()
    if voice_input:
        # Process the voice input through the NLP engine
        processUserInput(voice_input)
        # Update the UI with the new data
        renderUI()

# Function to start listening for voice commands
def start_voice_command_listener():
    try:
        while True:
            voice_command_handler()
    except KeyboardInterrupt:
        print("Voice command listener is stopping...")

# If this script is run directly, start the voice command listener
if __name__ == "__main__":
    start_voice_command_listener()
```