import re

# Define a function to generate a list of keywords from a phrase.
def generate_keywords(phrase):
    # Split the phrase into words.
    words = re.split(r"\s+", phrase)

    # Create a list of keywords.
    keywords = []
    for word in words:
        # Remove punctuation from the word.
        word = word.strip()

        # If the word is not empty, add it to the list of keywords.
        if word:
            keywords.append(word)

    # Return the list of keywords.
    return keywords

# Get the given phrase from the user.
phrase = input("Enter the given phrase: ")

# Generate a list of keywords from the phrase.
keywords = generate_keywords(phrase)

# Print the list of keywords to the console.
print("List of keywords:")
for keyword in keywords:
    print(keyword)

# Check if the list of keywords contains 1000 keywords.
if len(keywords) < 1000:
    print("The list of keywords contains less than 1000 keywords.")
else:
    print("The list of keywords contains 1000 keywords.")
