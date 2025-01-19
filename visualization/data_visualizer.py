import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from seaborn import histplot, heatmap


class DataVisualizer:
   """ Класс для визуализации данных. """
   
   def __init__(self):
      self.plots_created = 0  # отслеживание количества созданных графиков
   
   
   def plot_distribution(self, data: Series, title: str, x_label: str, color: str = 'blue'):
      """ Визуализация распределения данных. """
      self._check_data(data)
      plt.figure(figsize=(8, 6), num=title)
      histplot(data, kde=True, color=color)
      plt.title(title)
      plt.xlabel(x_label)
      plt.ylabel('Частота')
      plt.grid(True)
      plt.show()
      self.plots_created += 1
   
   
   def plot_correlation_matrix(self, corr_matrix: DataFrame, title: str):
      """ Визуализация корреляционной матрицы. """ 
      self._check_data(corr_matrix)
      plt.figure(figsize=(10, 8), num=title)
      heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
      plt.title(title)
      plt.show()
      self.plots_created += 1
   
   
   def total_plots(self):
      """ Возвращает количество созданных графиков """ 
      return self.plots_created
   
   
   def _check_data(self, data):
      """ Проверка данных перед построением графика """ 
      if data is None:
         raise ValueError('Данные для построения графика не предоставлены.')
      
      if not isinstance(data, (Series, DataFrame)):
         raise ValueError('Некорректный тип данных для построения графика.')
      
      if data.empty:
         raise ValueError('Данные пусты, невозможно построить график.')