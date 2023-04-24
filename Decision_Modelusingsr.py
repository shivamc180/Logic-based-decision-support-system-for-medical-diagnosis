import speech_recognition as sr
import pyaudio

# Define the symptoms and diseases
symptoms = ['fever', 'cough', 'fatigue', 'stomachache']
diseases = {
    'cold': ['fever', 'cough'],
    'flu': ['fever', 'fatigue'],
    'mono': ['headache', 'stomacheache']
}

# Define the logical rules for diagnosing diseases based on symptoms
def diagnose(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return 'cold'
    elif 'fever' in symptoms and 'cough' in symptoms and 'fatigue' in symptoms:
        return 'flu'
    elif 'fatigue' in symptoms and 'loss of appetite' in symptoms:
        return 'mono'
    else:
        return 'unknown'

# Initialize the voice recognition engine
r = sr.Recognizer()

# Get input from user's voice
with sr.Microphone() as source:
    print("Speak your symptoms:")
    audio = r.listen(source)

# Convert speech to text using Google Speech Recognition API
try:
    input_symptoms = r.recognize_google(audio).lower().split()
    print("Your symptoms are: " + str(input_symptoms))
except sr.UnknownValueError:
    print("Sorry, we could not understand your speech.")
    input_symptoms = []

# Make a diagnosis based on the input symptoms
if input_symptoms:
    disease = diagnose(input_symptoms)
    
    # Display the diagnosis
    if disease == 'unknown':
        print("Sorry, we could not diagnose your condition.")
    else:
        print("You may have " + disease + ".")
