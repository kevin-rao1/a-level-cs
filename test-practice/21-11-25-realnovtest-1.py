letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count1 = [0 for i in range(25)]
count2 = [0 for i in range(25)]
word1 = str(input("Enter first word: "))
word2 = str(input("Enter second word: "))
word1 = word1.lower()
word2 = word2.lower()
for letter in word1:
    for i in range(25):
        if letter == letters[i]:
            count1[i] = count1[i] + 1
print(count1)
for letter in word2:
    for i in range(25):
        if letter == letters[i]:
            count2[i] = count2[i] + 1
possible_to_form_word = True
for i in range(25):
    if count1[i] > count2[i]:
        possible_to_form_word = False

if possible_to_form_word == True:
    print("Possible to form word.")
else:
    print("Impossible to form word.")