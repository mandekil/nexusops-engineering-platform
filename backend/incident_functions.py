# CHALLENGE A
# Call function with input total attempts
failed_attempts_list = [2, 5, 9, 14]

def classify_severity(failed_attempts):
    if failed_attempts >= 10:
        return "Critical"
    elif failed_attempts >= 6:
        return "High"
    elif failed_attempts >= 3:
        return "Medium"
    else:
        return "Low"

# CHALLENGE B
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

for failed_attempt in failed_attempts_list:
    severity = classify_severity(failed_attempt)
    action = get_incident_action(severity)
    print("Failed Attempts:",failed_attempt,"| Severity:", severity, "| Action:", action)