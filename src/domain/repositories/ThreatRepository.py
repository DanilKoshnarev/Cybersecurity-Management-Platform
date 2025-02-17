class ThreatRepository:
    def save(self, threat):
        raise NotImplementedError

    def find_by_id(self, id):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError
