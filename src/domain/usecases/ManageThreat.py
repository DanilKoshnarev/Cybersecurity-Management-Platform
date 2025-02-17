from src.domain.entities.Threat import Threat

class ManageThreat:
    def __init__(self, threat_service):
        self.threat_service = threat_service

    def create_threat(self, id, name, type, severity):
        threat = Threat(id, name, type, severity)
        self.threat_service.add_threat(threat)

    def view_threat(self, id):
        return self.threat_service.get_threat(id)

    def view_all_threats(self):
        return self.threat_service.get_all_threats()

    def remove_threat(self, id):
        self.threat_service.delete_threat(id)
