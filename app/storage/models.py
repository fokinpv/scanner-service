from app.detectify import models


class Task:
    def __init__(self, domains, domains_info=None, id_=None):
        self.domains = domains
        self.domains_info = domains_info
        self.id = id_

    def as_detectify_domains(self):
        return [
            models.Domain(domain) for domain in self.domains
        ]
