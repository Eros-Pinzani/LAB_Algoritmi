from abc import ABC, abstractmethod

class StringMatcher(ABC):
    @abstractmethod
    def search(self, T: str, P: str):
        pass
