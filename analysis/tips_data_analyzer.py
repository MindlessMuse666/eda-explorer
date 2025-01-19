from os import system, name


class TipsDataAnalyzer:
    """ Основной класс для анализа данных о чаевых. """
    
    def __init__(self, data_loader, data_analyzer, data_visualizer):
        self.data_loader = data_loader
        self.data_analyzer = data_analyzer
        self.data_visualizer = data_visualizer


    def analyze_tips_data(self, url: str):
        """ Анализ данных о чаевых. """
        try:
            self.data_analyzer.load_and_process_data(url)
            
            system('cls' if name == 'nt' else 'clear') # Отчищаем консоль для эстетичного дебага
            
            print('Пропущенные значения:\n', self._format_missing_values(self.data_analyzer.check_missing_values()))
            print('\nСтатистика по числовым колонкам:\n', self.data_analyzer.calculate_numeric_summary())
            
            corr_matrix = self.data_analyzer.calculate_correlations()
            self.data_visualizer.plot_correlation_matrix(corr_matrix, 'Корреляционная матрица')
            
            self._visualize_key_metrics() # Визуализация распределения

            print(f'\nОбщее количество созданных графиков: {self.data_visualizer.total_plots()}')
        except ValueError as e:
            print(f'Ошибка: {e}')


    def _visualize_key_metrics(self):
        """ Визуализирует ключевые показатели, если они есть в данных. """
        if self.data_analyzer.data is not None:
            if 'tip' in self.data_analyzer.data.columns:
                self.data_visualizer.plot_distribution(self.data_analyzer.data['tip'], 'Распределение чаевых', 'Чаевые', 'green')
                
            if 'total_bill' in self.data_analyzer.data.columns:
                self.data_visualizer.plot_distribution(self.data_analyzer.data['total_bill'], 'Распределение общей суммы счёта', 'Общая сумма', 'purple')
    
    
    def _format_missing_values(self, missing_values):
        """ Форматирует вывод пропущенных значений. """
        return missing_values.to_frame(name='Количество').rename_axis('Колонка').reset_index()