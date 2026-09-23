LAST_NAME = "LANCION"
SEED_NUM = 5


def generate_signal():
    return f"{LAST_NAME}-{SEED_NUM} Signal 2026!"


def normalize_signal(signal):
    return signal.strip().upper()


def analyze_signal(signal):
    letters = 0
    numbers = 0
    spaces = 0
    special = 0

    print("\nCharacter Analysis:")

    for char in signal:
        if char.isalpha():
            category = "Letter"
            letters += 1
        elif char.isdigit():
            category = "Number"
            numbers += 1
        elif char.isspace():
            category = "Space"
            spaces += 1
        else:
            category = "Special Character"
            special += 1

        print(f"'{char}' -> {category}")

    return letters, numbers, spaces, special


def classify_signal(letters, numbers, spaces, special):
    if special > 0 and numbers > 0:
        return "COMPLEX SIGNAL"
    elif letters > numbers:
        return "TEXT-DOMINANT SIGNAL"
    elif numbers > letters:
        return "NUMBER-DOMINANT SIGNAL"
    else:
        return "BALANCED SIGNAL"


def main():
    signal = generate_signal()
    normalized = normalize_signal(signal)

    print("=== SIGNAL DIAGNOSTIC SYSTEM ===")
    print(f"Generated Signal: {signal}")
    print(f"Normalized Signal: {normalized}")

    letters, numbers, spaces, special = analyze_signal(normalized)

    classification = classify_signal(
        letters, numbers, spaces, special
    )

    print("\n=== DIAGNOSTIC REPORT ===")
    print(f"Letters: {letters}")
    print(f"Numbers: {numbers}")
    print(f"Spaces: {spaces}")
    print(f"Special Characters: {special}")
    print(f"Final Classification: {classification}")


if __name__ == "__main__":
    main()