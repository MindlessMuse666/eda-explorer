from abstractions.abstract_data_loader import DataLoader 
from pandas import DataFrame
from requests import get
from json import load

        
class JSONDataLoader(DataLoader):
    """ Класс для загрузки данных из JSON-файла. """
    
    def load_data(self, url: str) -> DataFrame:
        try:
            if url.startswith('http://') or url.startswith('https://'):
                response = get(url)
                response.raise_for_status()
                data = response.json()
            else:
                with open(url, 'r') as f:
                    data = load(f)
                    
            return DataFrame(data)
        except Exception as e:
            raise ValueError(f'Ошибка при загрузке JSON-файла: {e}')