# create function of classify_severity to return severity value
def classify_severity(failed_attempts):
    if failed_attempts >= 10:
        return "Critical"
    elif failed_attempts >= 6:
        return "High"
    elif failed_attempts >= 3:
        return "Medium"
    else:
        return "Low"

# CHALLENGE D
# Number 1
print("=== NexusOps Incident Validation ===")
user_input = input("Enter failed login attempts:")

try:
    failed_attempts = int(user_input)

    if failed_attempts < 0:
        print("Error: Failed attempts cannot be negative.")
    else:
        severity = classify_severity(failed_attempts)
        print("Severity:", severity)
except ValueError:
    print("Error: Please enter a valid whole number.")
