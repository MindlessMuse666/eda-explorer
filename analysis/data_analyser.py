from pandas import Series, DataFrame


class DataAnalyzer:
    """ Класс для анализа данных. """

    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.data = None


    def load_and_process_data(self, url: str):
        try:
            self.data = self.data_loader.load_data(url)
            
            if self.data.empty:
                raise ValueError('Загруженные данные пусты.')
        except ValueError as e:
            raise ValueError(f'Ошибка при загрузке и обработке данных: {e}')
        
        return self


    def check_missing_values(self) -> Series:
        """ Проверка пропущенных значений. """
        if self.data is None:
            raise ValueError('Данные не загружены.')
       
        return self.data.isnull().sum()
    
    
    def calculate_numeric_summary(self) -> DataFrame:
        """ Вычисление числовых сводок. """
        if self.data is None:
            raise ValueError('Данные не загружены.')
        
        return self.data.describe()


    def calculate_correlations(self) -> DataFrame:
        """ Вычисление корреляционной матрицы. """
        if self.data is None:
            raise ValueError('Данные не загружены.')
        
        numeric_data = self.data.select_dtypes(include=['number'])
        
        if numeric_data.empty:
            raise ValueError('Нет числовых данных для построения корреляций.')
        
        return numeric_data.corr()