from abc import ABC, abstractmethod

class IJsonSerializable(ABC):

    @abstractmethod
    def to_json(self) -> None:
        pass
