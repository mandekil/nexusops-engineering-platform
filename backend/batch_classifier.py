# Classifies multiple events and counts Critical incidents

# failed_attempts_list = [2, 4, 8, 12]
failed_attempts_list = [12, 8, 15, 4]
critical_count = 0

print("=== NexusOps Batch Classification ===")

for failed_attempts in failed_attempts_list:
    # Add classification logic here
    if failed_attempts >= 10:
        severity = "Critical"
        critical_count += 1
    elif failed_attempts >= 6:
        severity = "High"
    elif failed_attempts >= 3:
        severity = "Medium"
    else :
        severity = "Low"

    print("Failed Attempts:", failed_attempts, "| Severity:", severity)

print("Total Critical Incidents:", critical_count)