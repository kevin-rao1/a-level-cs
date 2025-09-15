name_list =  ['Ryansh', 'Oliver', 'Edward', 'Daniel', 'Alex', 'Ares', 'Thomas', 'Andy', 'Charlie', 'Ryan', 'Lucas']
scores_list = [[] for i in name_list]           # Create a lists of empty lists
while True:
    try:
        name = input("Enter name: ")                # Get the user to enter a name
        name_index = name_list.index(name)          # Find out which index that name appears at
        new_score = int(input("Enter score: "))     # The user enters a new score for that person
        scores_list[name_index].append(new_score)   # Append the new score to the list in the relevant location within scores
        print(f"New average score: {sum(scores_list[name_index])/len(scores_list[name_index])}")
    except ValueError:
        print("Name is not in list. Check spelling and capitalisation.")