class Domain:
    def __init__(self, name, properties=None):
        self.name = name
        self.properties = properties or {}

    def add_property(self, name, value):
        self.properties[name] = value

    def as_dict(self):
        return {
            'domain': self.name,
            'properties': self.properties
        }
