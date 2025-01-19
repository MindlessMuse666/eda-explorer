import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class DataLoader(ABC):
    """Абстрактный класс для загрузки данных."""
    @abstractmethod
    def load_data(self, url: str) -> pd.DataFrame:
        pass

class CSVDataLoader(DataLoader):
    """Класс для загрузки данных из CSV-файла."""
    def load_data(self, url: str) -> pd.DataFrame:
        try:
            return pd.read_csv(url)
        except Exception as e:
            raise ValueError(f"Ошибка при загрузке CSV-файла: {e}")

class DataAnalyzer:
    """Класс для анализа данных."""

    def __init__(self, data_loader: DataLoader):
        self.data_loader = data_loader
        self.data = None

    def load_and_process_data(self, url: str):
        try:
            self.data = self.data_loader.load_data(url)
            if self.data.empty:
                raise ValueError("Загруженные данные пусты.")
        except ValueError as e:
            raise ValueError(f"Ошибка при загрузке и обработке данных: {e}")
        return self

    def check_missing_values(self) -> pd.Series:
        """Проверка пропущенных значений."""
        if self.data is None:
           raise ValueError("Данные не загружены.")
        return self.data.isnull().sum()
    
    def calculate_numeric_summary(self) -> pd.DataFrame:
        """Вычисление числовых сводок."""
        if self.data is None:
            raise ValueError("Данные не загружены.")
        return self.data.describe()

    def calculate_correlations(self) -> pd.DataFrame:
        """Вычисление корреляционной матрицы."""
        if self.data is None:
            raise ValueError("Данные не загружены.")
        numeric_data = self.data.select_dtypes(include=['number'])
        if numeric_data.empty:
            raise ValueError("Нет числовых данных для построения корреляций.")
        return numeric_data.corr()

class DataVisualizer:
    """Класс для визуализации данных."""
    def __init__(self):
        self.plots_created = 0  # отслеживание количества созданных графиков
    
    def plot_distribution(self, data: pd.Series, title: str, x_label: str, color: str = "blue"):
            """Визуализация распределения данных."""
            self._check_data(data)
            plt.figure(figsize=(8, 6))
            sns.histplot(data, kde=True, color=color)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel("Частота")
            plt.grid(True)
            plt.show()
            self.plots_created += 1
    
    def plot_correlation_matrix(self, corr_matrix: pd.DataFrame, title: str):
            """Визуализация корреляционной матрицы."""
            self._check_data(corr_matrix)
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
            plt.title(title)
            plt.show()
            self.plots_created += 1
            
    def _check_data(self, data):
         """Проверка данных перед построением графика"""
         if data is None:
            raise ValueError("Данные для построения графика не предоставлены.")
         if not isinstance(data, (pd.Series, pd.DataFrame)):
            raise ValueError("Некорректный тип данных для построения графика.")
         if data.empty:
            raise ValueError("Данные пусты, невозможно построить график.")
    
    def total_plots(self):
       """Возвращает количество созданных графиков"""
       return self.plots_created
   
class SalesDataAnalyzer:
    """Основной класс для анализа данных о продажах."""
    def __init__(self, data_loader: DataLoader, data_analyzer: DataAnalyzer, data_visualizer: DataVisualizer):
        self.data_loader = data_loader
        self.data_analyzer = data_analyzer
        self.data_visualizer = data_visualizer

    def analyze_sales_data(self, url: str):
       try:
          self.data_analyzer.load_and_process_data(url)
          print("Пропущенные значения:\n", self.data_analyzer.check_missing_values())
          print("\nСтатистика по числовым колонкам:\n", self.data_analyzer.calculate_numeric_summary())
          
          corr_matrix = self.data_analyzer.calculate_correlations()
          self.data_visualizer.plot_correlation_matrix(corr_matrix, "Корреляционная матрица")
          
          # Визуализация распределения
          self._visualize_key_metrics()

          print(f"\nОбщее количество созданных графиков: {self.data_visualizer.total_plots()}")
       except ValueError as e:
          print(f"Ошибка: {e}")

    def _visualize_key_metrics(self):
         """Визуализирует ключевые показатели, если они есть в данных"""
         if self.data_analyzer.data is not None:
            if "revenue" in self.data_analyzer.data.columns:
                self.data_visualizer.plot_distribution(self.data_analyzer.data["revenue"], "Распределение выручки", "Выручка", "green")
            if "sales_quantity" in self.data_analyzer.data.columns:
                self.data_visualizer.plot_distribution(self.data_analyzer.data["sales_quantity"], "Распределение количества продаж", "Количество продаж", "purple")


# Пример использования
if __name__ == "__main__":
    csv_url = "https://raw.githubusercontent.com/plotly/datasets/master/sales_data.csv"
    data_loader = CSVDataLoader()
    data_analyzer = DataAnalyzer(data_loader)
    data_visualizer = DataVisualizer()
    sales_analyzer = SalesDataAnalyzer(data_loader, data_analyzer, data_visualizer)
    sales_analyzer.analyze_sales_data(csv_url)
