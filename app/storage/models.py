from app.detectify import models


class Task:
    def __init__(self, domains, results=None, id_=None):
        self.domains = domains
        self.results = results
        self.id = id_

    def as_dict(self):
        return {
            'domains': self.domains,
            'results': [item.as_dict() for item in self.results]
        }

    def as_detectify_domains(self):
        if self.results:
            return [
                models.Domain(domain.name, domain.properties)
                for domain in self.results
            ]

        return [
            models.Domain(domain)
            for domain in self.domains
        ]
