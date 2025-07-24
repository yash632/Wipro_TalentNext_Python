# Stream: Python
# Tech Module: Data Structure
# Project: 4
# Given a string of n words, help Alex to find out how many times his name
# appears in the string.
# Constraint: 1 <= n <= 200
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3
# Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex
# Bye Alex.
import re
text = "Hi Alex WelcomeAlex Bye Alex."
clean_text = re.sub(r'[^A-Za-z]', '', text)
count = 0
for i in range(len(clean_text) - 3):
    if clean_text[i:i+4] == "Alex":
        count += 1
print(count)
