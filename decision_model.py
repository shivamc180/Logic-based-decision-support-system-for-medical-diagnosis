# Define the symptoms and diseases
symptoms = ['fever', 'cough', 'fatigue', 'headache', 'stomachache']
diseases = {
    'cold': ['fever', 'cough'],
    'flu': ['fever', 'fatigue'],
    'viral': ['headache', 'stomachache']
}

# Define the logical rules for diagnosing diseases based on symptoms
def diagnose(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return 'cold'
    elif 'fever' in symptoms and 'fatigue' in symptoms:
        return 'flu'
    elif 'headache' in symptoms and 'stomachache' in symptoms:
        return 'viral'
    else:
        return 'unknown'

# Get input from user
print("Enter your symptoms (separated by spaces): ")
input_symptoms = input().split()

# Make a diagnosis based on the input symptoms
disease = diagnose(input_symptoms)

# Display the diagnosis
if disease == 'unknown':
    print("Sorry, we could not diagnose your condition.")
else:
    print("You may have " + disease + ".")
