# 1. Write a program to find check if a string has only octal digits. Given string ['789','123','004']

import re

strings = ['789', '123', '004']

pattern = re.compile(r'^[0-7]+$')

for s in strings:
    if pattern.match(s):
        print(f"{s} -> Valid Octal")
    else:
        print(f"{s} -> Invalid Octal")


# 2. Extract the user id, domain name and suffix from the following email addresses.

# emails = """zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com"""

import re

emails = ["zuck@facebook.com", "sunder33@google.com", "jeff42@amazon.com"]

pattern = re.compile(r'([\w\d]+)@([\w]+)\.([\w]+)')

for email in emails:
    match = pattern.match(email)
    if match:
        print(match.groups())



# 3. Split the following irregular sentence into proper words

# sentence = """A, very    very; irregular_sentence"""
# ## expected outout : A very very irregular sentence

import re

sentence = "A, very    very; irregular_sentence"

# Replace commas, semicolons, underscores with spaces
cleaned = re.sub(r'[,;_]', ' ', sentence)

# Remove multiple spaces
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

print(cleaned)


# 4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

# #tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
# http://t.co/lbwej0pX0d cc: @garybernhardt #rstats'''

# ##desired_output = 'Good advice What I would do differently if I was learning to code today'

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0pX0d cc: @garybernhardt #rstats'''

# Remove RT, cc, mentions, hashtags, URLs
tweet = re.sub(r'RT\s@\w+:', '', tweet)
tweet = re.sub(r'cc:\s*@\w+', '', tweet)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'http\S+', '', tweet)

# Clean extra spaces
tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)


# 5.Extract all the text portions between the tags from the following HTML page:

# https://raw.githubusercontent.com/selva86/datasets/master/sample.html


# Code to retrieve the HTML page is given below:

# import requests
# r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
# r.text  # html text is contained here

# desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 
# 'This is a Medium Header', 'This is a new paragraph!', 
# 'This is a another paragraph!', 
# 'This is a new sentence without a paragraph break, in bold italics.']

import re
import requests

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
html = r.text

# Extract text between tags
texts = re.findall(r'>([^<>]+)<', html)

# Remove unwanted whitespaces
texts = [t.strip() for t in texts if t.strip()]

print(texts)

# 6. Given the following list of words, write a Python program using Regular Expression to identify the words that begin and end with the same character.

# List of words:

# civic
# trust
# widows
# maximum
# museums
# aa
# as

import re

words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]

pattern = r"^([a-zA-Z]).*\1$"

matched_words = [word for word in words if re.match(pattern, word)]

print("Words that begin and end with the same character:")
print(matched_words)
