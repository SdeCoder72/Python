a = "Shanaya naaz"
print(len(a))
print(a.endswith("aya"))
print(a.endswith("kya"))
print(a.startswith("sh"))
print(a.startswith("Sha"))
print(a.capitalize())
print(a.title())


text = "  Hello World! Welcome to Python.  "

# Case Conversion
print(text.upper())        # ALL CAPS
print(text.lower())        # all lowercase
print(text.capitalize())   # First letter capitalized
print(text.title())        # Each word capitalized
print(text.swapcase())     # Swap case

# Searching and Counting
print(text.find("World"))  # Index of 'World'
print(text.index("Python"))# Index of 'Python'
print(text.count("o"))     # Count of 'o'

#  Replacing and Splitting
print(text.replace("Python", "Programming"))  # Replace word
print(text.split())        # Split into words
words = ["Python", "is", "fun"]
print(" ".join(words))     # Join words with space

# Trimming and Formatting
print(text.strip())        # Remove leading/trailing spaces
print(text.lstrip())       # Remove leading spaces
print(text.rstrip())       # Remove trailing spaces
print("My name is {} and I love {}".format("Shanaya", "Programming"))  # Format string

# ✅ Validation Checks
print("Python123".isalnum())  # True
print("Python".isalpha())     # True
print("12345".isdigit())      # True
print("   ".isspace())        # True