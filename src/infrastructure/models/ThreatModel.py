from src.domain.repositories.ThreatRepository import ThreatRepository

class ThreatModel(ThreatRepository):
    def __init__(self):
        self.threats = []

    def save(self, threat):
        self.threats.append(threat)

    def find_by_id(self, id):
        return next((threat for threat in self.threats if threat.id == id), None)

    def find_all(self):
        return self.threats

    def delete(self, id):
        self.threats = [threat for threat in self.threats if threat.id != id]
