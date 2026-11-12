class Incident:
    def __init__(self, incident_id, name, failed_attempts):
        self.incident_id = incident_id
        self.name = name
        self.failed_attempts = failed_attempts
        self.status = "Open"

    # CHALLENGE B TASK A DAY 4
    # create method inside class (showing object can perform operations)
    def update_status(self, new_status):
        self.status = new_status

    # CHALLENGE B TASK C DAY 4
    # create another method for classifying severity
    def classify(self):
        if self.failed_attempts >= 10:
            self.severity = "Critical"
        elif self.failed_attempts >= 6:
            self.severity = "High"
        elif self.failed_attempts >= 3:
            self.severity = "Medium"
        else:
            self.severity = "Low"