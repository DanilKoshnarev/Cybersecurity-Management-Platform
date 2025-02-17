class ThreatService:
    def __init__(self, threat_repository):
        self.threat_repository = threat_repository

    def add_threat(self, threat):
        self.threat_repository.save(threat)

    def get_threat(self, id):
        return self.threat_repository.find_by_id(id)

    def get_all_threats(self):
        return self.threat_repository.find_all()

    def delete_threat(self, id):
        self.threat_repository.delete(id)
