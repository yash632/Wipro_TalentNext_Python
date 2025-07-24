def ispalindrome(name):
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    result = []
    for k in sorted(freq.keys()):
        result.append(f"{k}-{freq[k]}")
    return "Frequency of letters: " + ", ".join(result)
