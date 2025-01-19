from analysis import DataAnalyzer, TipsDataAnalyzer
from visualization import DataVisualizer
from loaders import CSVDataLoader, JSONDataLoader
from json import dump


if __name__ == '__main__':
    """ Пример использования CSVDataLoader """
    csv_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
    data_loader = CSVDataLoader()
    data_analyzer = DataAnalyzer(data_loader)
    data_visualizer = DataVisualizer()
    tips_analyzer = TipsDataAnalyzer(data_loader, data_analyzer, data_visualizer)
    
    tips_analyzer.analyze_tips_data(csv_url)
    
    
    """ Пример использования JSONDataLoader """
    # json_url = 'test_data.json'
    # json_data = [{'tip': 1, 'total_bill': 15}, {'tip': 2, 'total_bill': 25}]
    # with open(json_url, 'w') as f:
    #     dump(json_data, f)
    # json_loader = JSONDataLoader()
    # data_analyzer_json = DataAnalyzer(json_loader)
    # data_visualizer_json = DataVisualizer()
    # tips_analyzer_json = TipsDataAnalyzer(json_loader, data_analyzer_json, data_visualizer_json)
    # tips_analyzer_json.analyze_tips_data(json_url)