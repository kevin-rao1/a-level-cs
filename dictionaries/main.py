import re
# Using the attached file as a starting point, write a function that creates a dictionary containing every word in the given string and the number of times it occurs.
bees_raw = ""
with open("files/bee20script.txt", "r") as bees_file:
    for line in bees_file:
        bees_raw = bees_raw + line
bees_raw = bees_raw.replace("\n", " ")
bees = re.sub(r"[^a-zA-Z0-9' ]", '', bees_raw)
bees = bees.lower()               # Convert to lowercase
word_list = bees.split()              # Create a list of words. By default split at every ' ' character.

# Get in dict form
word_frequency = {}
for word in word_list:
    word_frequency[word] = word_frequency.get(word, 0) +1 # get word frequency and increment, initialised at 0 if not already in list
# Sort the dict by value and print
wf_sorted = sorted(word_frequency, key=word_frequency.get, reverse=True)

print(2*"\n")
for word in wf_sorted[:5]:
    print(f"{word} appeared {word_frequency.get(word)} times.")