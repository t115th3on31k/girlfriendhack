```python
import speech_recognition as sr
from interpretation_engine.nlp_processing import processUserInput

# Initialize the recognizer
r = sr.Recognizer()

def record_voice_input():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        # Adjust the recognizer sensitivity to ambient noise
        r.adjust_for_ambient_noise(source)
        print("Listening for voice input...")
        # Listen for the first phrase and extract it into audio data
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            # Recognize speech using Google Speech Recognition
            voice_input = r.recognize_google(audio)
            print(f"Voice input received: {voice_input}")
            return voice_input
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def voice_input_to_text():
    voice_input = record_voice_input()
    if voice_input:
        # Process the voice input through the NLP engine
        processUserInput(voice_input)
    else:
        print("No voice input detected.")

# Example usage:
if __name__ == "__main__":
    voice_input_to_text()
```