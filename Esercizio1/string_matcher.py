from abc import ABC, abstractmethod

class StringMatcher(ABC):
    @abstractmethod
    def search(self, text: str, pattern: str):
        pass
