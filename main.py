import numpy as np
from time import time

from api_collector import api_get
from counter import letter_appearance
from char_finder import chars_from, origins_from

# Part 1

# We get the data from the API
# Print loadings to see progress
print("Getting data locations...")
locations = api_get("location")
print("Getting data characters...")
characters = api_get("character")
print("Getting data episodes...\n")
episodes = api_get("episode")
print("Done!\n")

# We count the letter appearances
locations_count = letter_appearance("l", locations)
characters_count = letter_appearance("c", characters)
episodes_count = letter_appearance("e", episodes)

# Display results
print(f"The letter \"l\" appears {locations_count} in location names.")
print(f"The letter \"c\" appears {characters_count} in character names.")
print(f"The letter \"e\" appears {episodes_count} in episode names.\n")

# Part 2

# Make numpy array from characters list to make faster operations
characters_array = np.array(characters)
aux_chars = chars_from(episodes[0], characters_array)
# print(aux_chars)
print(origins_from(aux_chars))
# print(episodes[0]["characters"])

