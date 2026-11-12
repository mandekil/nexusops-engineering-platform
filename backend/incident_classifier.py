# Classifies an individual incident

# INDEPENDENT CHALLENGE 1 ===============================
# Number 1
incident_name = "Multiple Failed Login Attempts"
# Number 2
incident_id = 1002
# Number 3
failed_attempts = 12
# =======================================================

status = "Open"
is_resolved = False

# INDEPENDENT CHALLENGE 2 ===============================
# Number 1
if failed_attempts >=10:
    severity = "Critical"
# Number 2
elif failed_attempts >= 6:
    severity = "High"
# Number 3
elif failed_attempts >= 3:
    severity = "Medium"
# Number 4
else :
    severity = "Low"
# =======================================================

print("=== NexusOps Incident ===")
print("Incident ID:", incident_id)
print("Incident:", incident_name)
print("Status:", status)
print("Resolved:", is_resolved)
# INDEPENDENT CHALLENGE 1 ===============================
# Number 4 ==============================================
print("Failed Attempt(s):", failed_attempts)
# =======================================================
# INDEPENDENT CHALLENGE 2 ===============================
# Number 5 ==============================================
print("Severity:", severity)
# =======================================================