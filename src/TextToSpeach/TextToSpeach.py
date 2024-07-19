from gtts import gTTS
import os

def text_to_speech(text, language='tr', output_file='output.mp3'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the speech to a file
    tts.save(output_file)
    
    # Optionally, play the file
    # os.system(f"start {output_file}") # For Windows
    # os.system(f"afplay {output_file}") # For MacOS
    # os.system(f"mpg321 {output_file}") # For Linux

if __name__ == "__main__":
    text = "Kafanı sikiyim bora"
    language = 'tr'
    output_file = 'output.mp3'
    
    text_to_speech(text, language, output_file)
    print(f"Speech saved to {output_file}")
