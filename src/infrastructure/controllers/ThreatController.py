class ThreatController:
    def __init__(self, manage_threat):
        self.manage_threat = manage_threat

    def add_threat(self, id, name, type, severity):
        self.manage_threat.create_threat(id, name, type, severity)

    def get_threat(self, id):
        return self.manage_threat.view_threat(id)

    def get_all_threats(self):
        return self.manage_threat.view_all_threats()

    def delete_threat(self, id):
        self.manage_threat.remove_threat(id)
