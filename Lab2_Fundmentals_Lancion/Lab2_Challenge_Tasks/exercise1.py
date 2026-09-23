import random

surname = "Lancion"
SEED_NUM = 5  

random.seed(SEED_NUM + sum(ord(c) for c in surname))

# Generate 8 sensor readings, including possible invalid entries
sensor_data = [
    str(random.randint(0, 100)),
    str(random.randint(0, 100)),
    "abc",
    str(random.randint(0, 100)),
    "-5",
    str(random.randint(0, 100)),
    "error",
    str(random.randint(0, 100))
]

print("=== SENSOR MONITORING SYSTEM ===")
print("Generated Sensor Data:")
print(sensor_data)

valid_results = []
invalid_results = []
classifications = []

for entry in sensor_data:
    try:
        value = float(entry)

        if value < 0 or value > 100:
            invalid_results.append(entry)
            print(f"{entry} -> INVALID")
        else:
            valid_results.append(value)

            if value < 30:
                classification = "LOW"
            elif value <= 70:
                classification = "NORMAL"
            else:
                classification = "HIGH"

            classifications.append((value, classification))
            print(f"{entry} -> VALID -> {classification}")

    except ValueError:
        invalid_results.append(entry)
        print(f"{entry} -> INVALID")

print("\n=== SUMMARY ===")
print("Valid Readings:", len(valid_results))
print("Invalid Readings:", len(invalid_results))

print("\nClassification Results:")
for value, classification in classifications:
    print(f"{value} -> {classification}")

print("\nExecution Log:")
print("Sensor data generated.")
print("All readings validated and classified.")

print("\nFinal Output:")
print(f"Processed {len(sensor_data)} readings.")
print(f"Valid: {len(valid_results)} | Invalid: {len(invalid_results)}")