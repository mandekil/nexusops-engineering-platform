from incident_model import Incident

incident = Incident(1001, "Suspicious Login", 8)

print ("Initial status:", incident.status)

incident.update_status("Investigating")

print("Updated status:", incident.status)

try:
    incident.update_status("Deleted")
except ValueError as error:
    print("Validation error:", error)

print("Final status:", incident.status)