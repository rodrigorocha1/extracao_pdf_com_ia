from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class IoperacaoDados(ABC,  Generic[T]):

    @abstractmethod
    def gerar_dados(self, reposta_ia: T):
        pass

    @abstractmethod
    def salvar_dados(self):
        pass
