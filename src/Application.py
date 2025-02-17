from src.domain.entities.Threat import Threat
from src.domain.repositories.ThreatRepository import ThreatRepository
from src.domain.services.ThreatService import ThreatService
from src.domain.usecases.ManageThreat import ManageThreat
from src.infrastructure.models.ThreatModel import ThreatModel
from src.infrastructure.controllers.ThreatController import ThreatController

def main():
    threat_repository = ThreatModel()
    threat_service = ThreatService(threat_repository)
    manage_threat = ManageThreat(threat_service)
    threat_controller = ThreatController(manage_threat)

    
    threat_controller.add_threat("1", "SQL Injection", "Injection", "High")
    threat_controller.add_threat("2", "Cross-Site Scripting", "XSS", "Medium")

    
    for threat in threat_controller.get_all_threats():
        print(f"ID: {threat.id}, Name: {threat.name}, Type: {threat.type}, Severity: {threat.severity}")

    
    threat_controller.delete_threat("1")

  
    for threat in threat_controller.get_all_threats():
        print(f"ID: {threat.id}, Name: {threat.name}, Type: {threat.type}, Severity: {threat.severity}")

if __name__ == "__main__":
    main()
