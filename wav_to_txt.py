import speech_recognition as sr

recognizer = sr.Recognizer()

file = "file.wav"

with sr.AudioFile(file) as source:
    data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(data)

        # Write the recognized text to a .txt file
        with open("output.txt", "w") as txt_file:
            txt_file.write(text)

        print("Speech recognition results written to output.txt")

    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from service; {e}")
