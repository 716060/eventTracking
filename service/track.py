import abc

class Track(metaclass=abc.ABCMeta):
    def __init__(self):
        self.superior = None

    def set_superior(self, superior):
        self.superior = superior

    @abc.abstractmethod
    def handleRequest(self, event, results):
        pass
