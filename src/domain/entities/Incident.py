class Incident:
    def __init__(self, id, threat_id, description, timestamp, status):
        self.id = id
        self.threat_id = threat_id
        self.description = description
        self.timestamp = timestamp
        self.status = status
