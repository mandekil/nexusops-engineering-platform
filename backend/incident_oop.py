# IMPORT MOVED CLASS TO BE ABLE TO USE HERE
from incident_model import Incident

# CHALLENGE A DAY 4
incident_1 = Incident(1001, "Suspicious Login", 4)
incident_2 = Incident(1002, "Multiple Failed Login", 12)
incident_3 = Incident(1003, "Unusual Network Traffic", 7)

# CHALLENGE B TASK A DAY 4
# updating objects
incident_1.update_status("Investigating")
incident_2.update_status("Escalated")

incidents_list = [
    incident_1,
    incident_2,
    incident_3
]

# CHALLENGE A & B TASK C DAY 4
# CHALLENGE A to display each object using for loop
# CHALLENGE B TASK C to display each object with additional information of severity and status
print("=== NexusOps Incident Objects ===")
print()
for incident in incidents_list:
    incident.classify()

    print("ID:", incident.incident_id, "| Name:", incident.name, "| Attempts:", incident.failed_attempts, "| Severity:", incident.severity, "| Status:", incident.status)

print()
print("Total Incidents:", len(incidents_list))
# print(incident_1.classify())