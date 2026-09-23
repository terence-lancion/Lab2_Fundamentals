import random

surname = "Lancion"
SEED_NUM = 5  

random.seed(SEED_NUM + sum(ord(c) for c in surname))

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#"
signal = "".join(random.choice(characters) for _ in range(15))

print("=== SIGNAL DIAGNOSTIC SYSTEM ===")
print("Generated Signal:", repr(signal))

# Normalize the signal
processed_signal = signal.strip().upper()

print("Processed Signal:", repr(processed_signal))

letters = 0
numbers = 0
spaces = 0
special = 0

print("\nCharacter Analysis:")

for char in processed_signal:
    if char.isalpha():
        category = "LETTER"
        letters += 1
    elif char.isdigit():
        category = "NUMBER"
        numbers += 1
    elif char.isspace():
        category = "SPACE"
        spaces += 1
    else:
        category = "SPECIAL CHARACTER"
        special += 1

    print(f"{repr(char)} -> {category}")

total = len(processed_signal)

if letters > numbers and letters > special:
    classification = "ALPHABETIC-DOMINANT"
elif numbers > letters and numbers > special:
    classification = "NUMERIC-DOMINANT"
else:
    classification = "MIXED SIGNAL"

print("\n=== DIAGNOSTIC REPORT ===")
print("Letters:", letters)
print("Numbers:", numbers)
print("Spaces:", spaces)
print("Special Characters:", special)
print("Signal Classification:", classification)

print("\nExecution Log:")
print("Signal generated.")
print("Signal normalized.")
print("Signal analyzed character by character.")

print("\nFinal Output:")
print("Signal analysis completed successfully.")
print("Classification:", classification)