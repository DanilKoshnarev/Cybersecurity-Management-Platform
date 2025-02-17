import unittest
from src.domain.entities.Threat import Threat
from src.infrastructure.models.ThreatModel import ThreatModel
from src.domain.services.ThreatService import ThreatService
from src.domain.usecases.ManageThreat import ManageThreat

class ThreatManagementTests(unittest.TestCase):
    def setUp(self):
        self.threat_repository = ThreatModel()
        self.threat_service = ThreatService(self.threat_repository)
        self.manage_threat = ManageThreat(self.threat_service)

    def test_create_threat(self):
        self.manage_threat.create_threat("1", "SQL Injection", "Injection", "High")
        threat = self.manage_threat.view_threat("1")
        self.assertIsNotNone(threat)
        self.assertEqual(threat.name, "SQL Injection")
        self.assertEqual(threat.type, "Injection")
        self.assertEqual(threat.severity, "High")

    def test_delete_threat(self):
        self.manage_threat.create_threat("1", "SQL Injection", "Injection", "High")
        self.manage_threat.remove_threat("1")
        threat = self.manage_threat.view_threat("1")
        self.assertIsNone(threat)

    def test_view_all_threats(self):
        self.manage_threat.create_threat("1", "SQL Injection", "Injection", "High")
        self.manage_threat.create_threat("2", "Cross-Site Scripting", "XSS", "Medium")
        threats = self.manage_threat.view_all_threats()
        self.assertEqual(len(threats), 2)

if __name__ == "__main__":
    unittest.main()
