from abc import ABC, abstractmethod
from typing import Any 

class GenericAlgo(ABC):

    @abstractmethod
    def run(self) -> Any:
        pass
    
    @abstractmethod
    def test(self):
        pass
    
