from abc import ABC, abstractmethod


class ParentClass(ABC):

    @abstractmethod
    def method(self):
        pass
