import speech_recognition as sr

class SpeechToText:
    def __init__(self, language='en-US'):
        self.recognizer = sr.Recognizer()
        self.language = language

    def listen(self, source):
        print("Listening...")
        audio = self.recognizer.listen(source)
        return audio

    def recognize(self, audio):
        try:
            print("Recognizing...")
            # Print the raw audio data
            audio_data = audio.get_wav_data()
            print(f"Raw Audio Data: {audio_data[:100]}...")  # Printing first 100 bytes for brevity
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    def record_and_recognize(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.listen(source)
            return self.recognize(audio)

# Example usage
if __name__ == "__main__":
    stt = SpeechToText(language='en-US')
    text = stt.record_and_recognize()
    print(f"Final Recognized Text: {text}")
