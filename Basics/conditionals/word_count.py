# Detect duplicate characters in a string.
from collections import Counter


# Find duplicate characters
char = []
while True:
  name = input("Enter a word or 'q' to quit: ")
  if name.lower() == "q":
    print("Exiting...")
    break

  for x in name:
    if name.count(x) >= 1:
      char.append(x)

  # Display duplicate characters
  duplicates = Counter([ch for ch in char])
  if duplicates:
    print("Duplicate characters found:")
    for ch, count in duplicates.items():
      if count > 1:
        print(f"Character: '{ch}' - Count: {count}")
  else:
    print("No duplicate characters found.")