# 1. Write a program to read the entire content from a txt file and display it to the user.

with open("file.txt", "r") as f:
    print(f.read())
# 2. Write a program to read first n lines from a txt file. Get n as user input.

n = int(input())
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
# 3. Write a program to accept input from user and append it to a txt file.

data = input()
with open("file.txt", "a") as f:
    f.write(data + "\n")
# 4. Write a program to read contents from a txt file line by line and store each line into a list.

with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

with open("file.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print(longest)
# 6. Write a program to count the frequency of a user entered word in a txt file.

word = input()
with open("file.txt", "r") as f:
    text = f.read().split()
count = text.count(word)
print(count)
