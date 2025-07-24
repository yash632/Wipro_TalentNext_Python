import sys

if len(sys.argv) != 4:
    print("Usage: python project.py <like-numbers> <dislike-numbers> <given-numbers>")
    sys.exit(1)

like = set(sys.argv[1].split('-'))
dislike = set(sys.argv[2].split('-'))
nums = sys.argv[3].split('-')

happiness = 0

for num in nums:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print(happiness)
