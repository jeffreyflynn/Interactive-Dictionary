import json

# Load the dictionary data
data = json.load(open("data.json"))

# Function for retrieving the definition of a word
def find_definition(word):
  return data[word]

# Variable representing the user input
user_input = input("Enter a word: ")

# Retrieve the definition or the user input
print(find_definition(user_input))