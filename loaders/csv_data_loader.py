from abstractions.abstract_data_loader import DataLoader 
from pandas import DataFrame, read_csv


class CSVDataLoader(DataLoader):
    """ Класс для загрузки данных из CSV-файла. """
    
    def load_data(self, url: str) -> DataFrame:
        try:
            return read_csv(url)
        except Exception as e:
            raise ValueError(f'Ошибка при загрузке CSV-файла: {e}')