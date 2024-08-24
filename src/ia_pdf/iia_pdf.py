from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class IIApdf(ABC, Generic[T]):

    @abstractmethod
    def obter_texto(self) -> T:
        pass
