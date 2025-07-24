#Q. Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen. Next, change a fact about one of
# the people. Also add an additional person and corresponding fact. Display the new list of people
# and facts. Run the program multiple times and notice if the order changes.
# Sample output:
# Jeff: Is afraid of Dogs.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jeff: Is afraid of heights.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jill: Can hula dance.
people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


print("Original list:\n")
for name, fact in people.items():
    print(f"{name}: {fact}")


people["Jeff"] = "Is afraid of heights."


people["Jill"] = "Can hula dance."


print("\nUpdated list:\n")
for name, fact in people.items():
    print(f"{name}: {fact}")
