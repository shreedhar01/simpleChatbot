import speech_recognition as sr

def get_audio_input():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        
        # Adjust for ambient noise and set a timeout
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.dynamic_energy_threshold = True
        
        try:
            # Listen for audio input
            audio = recognizer.listen(source, timeout=5)
            
            print("Processing...")
            
            # Use Google's speech recognition
            text = recognizer.recognize_google(audio)
            
            print(f"You said: {text}")
            return text
        
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
            return None
            