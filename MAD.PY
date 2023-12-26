import random

def madlibs():
    # Lists of words
    nouns = ['cat', 'dog', 'house', 'book']
    verbs = ['run', 'jump', 'sing', 'dance']
    adjectives = ['happy', 'sad', 'funny', 'colorful']

    # Mad Libs template
    # template = "The {adjective} {noun} likes to {verb}."

    # Randomly select words
    selected_noun = random.choice(nouns)
    selected_verb = random.choice(verbs)
    selected_adjective = random.choice(adjectives)

    # Replace placeholders in the template using f-strings
    madlibs_text = f"The {selected_adjective} {selected_noun} likes to {selected_verb}."

    # Print the generated Mad Libs story
    print(madlibs_text)

# Call the function to generate and display a Mad Libs story
madlibs()
