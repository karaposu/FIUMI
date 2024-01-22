import openai
import random

# Define your features
features = {
    "First Name": ["Alex", "Maria", "John", "Lina", "Ahmed", "Yuki", "Emma", ...],
    "Last Name": ["Smith", "Johnson", "Kumar", "Tanaka", "Schneider", "Garcia", "Hassan", ...],
    "Age": range(18, 70),
    "Gender": ["Male", "Female", "Non-Binary"],
    "Nationality": ["USA", "Germany", "Brazil", "Japan", "Egypt", "India", ...],
    "Language": ["English", "German", "Portuguese", "Japanese", "Arabic", "Hindi", ...],
    "Education Level": ["High School", "Bachelor's", "Master's", "PhD"],
    "Occupation": ["Engineer", "Artist", "Teacher", "Doctor", "Researcher", ...],
    "Interests": ["Sports", "Art", "Technology", "Literature", "Travel", "Cooking", ...],
    "Personality Traits": ["Introvert", "Extrovert", "Ambivert"],
    "Body Type": ["Slim", "Athletic", "Average", "Curvy", "Muscular"],
    
    "Eye Features": {
        "Eye Color": ["Blue", "Brown", "Green", "Hazel", "Grey", "Amber"],
        "Eye Shape": ["Almond", "Round", "Monolid", "Hooded", "Upturned", "Downturned"]
    },

    "Hair Features": {
        "Hair Color": ["Black", "Brown", "Blonde", "Red", "Grey", "White", "Dyed"],
        "Hair Type": ["Straight", "Wavy", "Curly", "Kinky"],
        "Hair Length": ["Bald", "Short", "Medium", "Long", "Very long"]
    },

    "Lip Features": {
        "Lip Shape": ["Full", "Thin", "Wide", "Small", "Heart-shaped", "Round"],
        "Lip Size": ["Small", "Medium", "Large"]
    },

    "Beard Features": {
        "Beard Style": ["Clean-shaven", "Stubble", "Goatee", "Full beard", "Moustache", "Sideburns"],
        "Beard Length": ["Short", "Medium", "Long", "Very long"]
    },

    "Skin Color": ["Pale", "Fair", "Olive", "Tan", "Brown", "Dark"],
    "Skin Imperfections": ["Freckles", "Moles", "Scars", "Acne", "None"],
    "Chest Features": ["Flat", "Average", "Muscular", "Broad"],
    "Attractiveness": ["Average", "Above average", "Below average"],
    "Posing Habit": ["Formal pose", "Casual pose", "Dynamic pose", "Relaxed pose"],
    "Body Hair": ["None", "Some", "Average", "Abundant"],
    "Fashion Style": ["Casual", "Business", "Sporty", "Hipster", "Elegant", "Bohemian"],
    "Eyebrow Features": ["Thick", "Thin", "Arched", "Straight", "Bushy", "Well-groomed"],
    
    # Additional Features can be added as needed
}
}

# Function to create a random persona feature set
def create_feature_set():
    persona = {
        "First Name": random.choice(features["First Name"]),
        "Last Name": random.choice(features["Last Name"]),
        # ... [other features] ...
    }
    return persona

# Function to generate persona description using GPT-4
def generate_persona_description(persona):
    # Constructing the prompt
    prompt = "Create a detailed description for a persona with the following features:\n"
    for feature, value in persona.items():
        prompt += f"{feature}: {value}\n"

    # Adding instruction for GPT-4
    prompt += "\nGenerate a coherent and detailed background story for this persona:"

    try:
        # OpenAI API call (make sure to replace 'your_api_key' with your actual API key)
        openai.api_key = 'your_api_key'
        response = openai.Completion.create(
            model="text-davinci-004",  # Replace with GPT-4 model name when available
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Creating a random feature set
random_persona = create_feature_set()

# Generating persona description
description = generate_persona_description(random_persona)
print(description)

