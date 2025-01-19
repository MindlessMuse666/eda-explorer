from abc import ABC, abstractmethod
from pandas import DataFrame


class DataLoader(ABC):
    """ Абстрактный класс для загрузки данных. """
    
    @abstractmethod
    def load_data(self, url: str) -> DataFrame:
        pass