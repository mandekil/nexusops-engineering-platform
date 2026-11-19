import json

incident = {
    "id" : 1001,
    "name" : "Suspicious Login",
    "severity" : "High",
    "status" : "Open",
    "assigned_to" : None
}

json_data = json.dumps(incident)
python_data = json.loads(json_data)
print("JSON Data:", json_data)
print("Python Data:", python_data)
print("Incident Name:", python_data["name"])