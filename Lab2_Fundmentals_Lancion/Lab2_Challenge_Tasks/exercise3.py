import random

surname = "Lancion"
SEED_NUM = 5  

random.seed(SEED_NUM + sum(ord(c) for c in surname))

# Generate a unique password
password = surname[:3].upper() + str(random.randint(100, 999))

# Generate attempt limit
attempt_limit = random.randint(3, 5)

print("=== AUTHENTICATION SYSTEM ===")
print("Generated Password:", password)
print("Attempt Limit:", attempt_limit)

# Simulated attempts
attempts = [
    "wrong123",
    "password",
    password
]

attempts_made = 0
access_granted = False

print("\n=== EXECUTION LOG ===")

for attempt in attempts:
    if attempts_made >= attempt_limit:
        break

    attempts_made += 1
    print(f"Attempt {attempts_made}: {attempt}")

    if attempt == password:
        print("Access Granted.")
        access_granted = True
        break
    else:
        print("Incorrect Password.")

if access_granted:
    access_result = "ACCESS GRANTED"
    final_state = "SYSTEM UNLOCKED"
else:
    access_result = "ACCESS DENIED"
    final_state = "SYSTEM LOCKED"

print("\n=== FINAL OUTPUT ===")
print("Generated Password:", password)
print("Attempt Limit:", attempt_limit)
print("Attempts Made:", attempts_made)
print("Access Result:", access_result)
print("Final System State:", final_state)