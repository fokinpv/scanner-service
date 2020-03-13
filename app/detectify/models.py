class Domain:
    def __init__(self, name, properties=None):
        self.name = name
        self.properties = properties or {}

    def __str__(self):
        return f'{self.name}\n {self.properties}'

    def add_property(self, name, value):
        self.properties[name] = value

    def as_dict(self):
        return {
            'domain': self.name,
            'properties': self.properties
        }
