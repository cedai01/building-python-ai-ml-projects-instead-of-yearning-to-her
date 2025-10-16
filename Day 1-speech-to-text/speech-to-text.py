import speech_recognition as sr

def record_voice():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as live_mic:
        # Adjust for background noise to improve accuracy
        recognizer.adjust_for_ambient_noise(live_mic)

        print("Please say something:")
        # Listen for user’s speech from the microphone
        audio = recognizer.listen(live_mic)

        try:
            # Use Google’s speech recognition to convert audio to text
            phrase = recognizer.recognize_google(audio)
            return phrase
        except sr.UnknownValueError:
            # Handle unrecognized speech
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            # Handle connection errors (e.g., if Google API is down)
            return "Sorry, there was an issue with the speech recognition service."

if __name__ == "__main__":
    # Run the function and store the recognized text
    phrase = record_voice()

    # Save the recognized text to a file
    with open("output.txt", "w") as file:
        file.write(phrase)

    # Display the recognized text in the console
    print("The last sentence you spoke was:")
    print(phrase)
