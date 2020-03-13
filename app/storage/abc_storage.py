class Storage:
    def get(self, id_):
        raise NotImplementedError

    def get_list(self, limit):
        raise NotImplementedError

    def add(self, task):
        raise NotImplementedError

    def update(self, task):
        raise NotImplementedError
