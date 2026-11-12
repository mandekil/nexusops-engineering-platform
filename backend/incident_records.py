incident = {
    "id": 1001,
    "name": "Multiple Failed Login Attempts",
    "failed_attempts": 8,
    "status": "Open"
}

# CHALLENGE C
# Number 2
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

# BONUS CHALLENGE
# Returns the appropriate action based on severity
def get_incident_action(severity):
    if severity == "Critical":
        return "Immediate escalation"
    elif severity == "High":
        return "Escalate to Security Analyst"
    elif severity == "Medium":
        return "Schedule investigation"
    else:
        return "Monitor incident"

# Number 3 & 4
# create value of incident["severity"] from the returned severity
incident["severity"] = classify_severity(incident["failed_attempts"])

# Number 5
# update incident status open to investigating
incident["status"] = "Investigating"

# BONUS CHALLENGE
incident["action"] = get_incident_action(incident["severity"])

print("=== NexusOps Incident Record ===")
# Number 1
print("Incident ID:",incident["id"])
print("Incident Name:",incident["name"])
# Number 6
print("Failed Attempts:", incident["failed_attempts"])
print("Severity:", incident["severity"])
print("Status:", incident["status"])
# BONUS CHALLENGE
print("Action:", incident["action"])