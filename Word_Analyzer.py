import string

print("Welcome to the Word Analyzer!")
total_text = input("Type in here to test it out!: ")

punctuation = 0
digits = 0
spaces = 0
lowercase_letters = 0
uppercase_letters = 0

for char in total_text:
    if char in string.punctuation:
        punctuation += 1
    elif char in string.digits:
        digits += 1
    elif char in string.ascii_lowercase:
        lowercase_letters += 1
    elif char in string.ascii_uppercase:
        uppercase_letters += 1
    elif char in string.whitespace:
        spaces += 1

full_total = punctuation + digits + lowercase_letters + uppercase_letters + spaces

if full_total == len(total_text):
    print("Everything looks good! The result is correct! ✅")
else:
    print("WARNING: The result is incorrect! If you know Python, you can fix it! ❌")
    question = input("Would you like to try again? (yes/no): ")
    if question.lower() == "yes":
        exec(open("Word_Analyzer.py").read())
    else:
        print("Thank you for using the Word Analyzer. Goodbye!")

print(" ")

print(
    f"After careful analysis, here are the results:\n"
    f"Punctuation marks: {punctuation}\n"
    f"Digits: {digits}\n"
    f"Lowercase letters: {lowercase_letters}\n"
    f"Uppercase letters: {uppercase_letters}\n"
    f"Spaces: {spaces}"
)
input("Press Enter to exit the program.")