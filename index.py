import json

# Load the dictionary data
data = json.load(open("data.json"))

# Function for retrieving the definition of a word
def find_definition(word):
  # Check if the word exists in our data
  if word in data:
    return data[word]
  else:
    return "This word does not exist in the data."

# Variable representing the user input
user_input = input("Enter a word: ")

# Retrieve the definition or the user input
print(find_definition(user_input))