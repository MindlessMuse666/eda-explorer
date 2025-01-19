# Исследование EDA (EDA Explorer) <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT-License image"></a>

Этот проект представляет собой инструмент на Python для **разведочного анализа данных (EDA)** и **визуализации**. Он разработан с целью предоставить модульное и расширяемое решение для исследования наборов данных, следуя принципам ООП. Этот проект является практической работой.

- **Тема практической работы:** `Обнаружение и визуализация данных для понимания их сущности`
- **Дисциплина:** `МДК 13.01: Основы применения методов искусственного интеллекта в программировании`


## Возможности

- **Загрузка данных:** Поддерживает загрузку данных как из **CSV, так и из JSON** файлов, как из локальных путей, так и по URL.
- **Анализ данных:** Выполняет основные операции EDA, включая:
  - Проверку на наличие пропущенных значений.
  - Расчет описательных статистик для числовых данных.
  - Вычисление корреляционных матриц для понимания взаимосвязей между переменными.
- **Визуализация данных:** Создает наглядные визуализации, такие как:
  - Гистограммы для отображения распределений отдельных переменных.
  - Тепловые карты для визуализации корреляционных матриц.
- **Модульность и расширяемость:** Реализован с акцентом на модульность, используя принципы ООП для упрощения сопровождения и расширения.
- **Обработка ошибок:** Включена надежная обработка ошибок для корректного управления различными сценариями, включая некорректные форматы файлов, отсутствующие данные и проблемы с сетью.


## Скриншоты работы

### [main.py](main.py)
![image](https://github.com/user-attachments/assets/a232cf35-b2ca-429f-835e-d930e5e00d1c)

### Корреляционная матрица
![image](https://github.com/user-attachments/assets/f7b7f263-1d3a-4aa6-8952-0dcbb833994c)
### График распределения чаевых
![image](https://github.com/user-attachments/assets/f1dd7e51-0ede-4339-9bb7-9fe3b4f1d7e5)
### График распределения общей суммы счёта
![image](https://github.com/user-attachments/assets/ddcac76f-cf5a-47d4-9e7a-9daf0209c8ab)


## Используемые технологии

- `Python`
- `Pandas`
- `Seaborn`
- `Matplotlib`
- `Requests`


## Структура проекта

### Дерево проекта
```
eda-explorer/
├── abstractions/
│   └── abstract_data_loader.py
├── analysis/
│   ├── data_analyser.py
│   └── tips_data_analyzer.py
├── loaders/
│   ├── csv_data_loader.py
│   └── json_data_loader.py
├── visualization/
│   └── data_visualizer.py
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

### Главные скрипты проекта
- [__init__.py](__init__.py): Делает eda-explorer пакетом Python.
- [abstract_data_loader.py](abstractions/abstract_data_loader.py): Определяет абстрактный класс DataLoader и конкретные классы для загрузки данных (CSVDataLoader, JSONDataLoader).
- [data_analyzer.py](analysis\data_analyzer.py): Определяет класс DataAnalyzer для выполнения операций EDA.
- [tips_data_analyzer.py](analysis/tips_data_analyzer.py): Определяет класс TipsDataAnalyzer для координации процесса анализа и визуализации данных, конкретно для данных о чаевых.
- [data_visualizer.py](visualization\data_visualizer.py): Определяет класс DataVisualizer для создания визуализаций.
- [main.py](main.py): Основной скрипт для запуска анализа и визуализации.


## Начало работы

1. Склонируйте репозиторий:

```bash
git clone https://github.com/MindlessMuse666/eda-explorer
```

2. Перейдите в директорию проекта:
  
```bash
cd eda-explorer
```

3. Установите необходимые пакеты с помощью [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

4. Запустите основной скрипт:

```bash
python main.py
```


## Вклад

Приветствуются любые вклады! Не стесняйтесь открывать **issues** или отправлять **pull requests**.


## Лицензия

Этот проект распространяется под лицензией MIT - смотрите файл [LICENSE](LICENSE) для деталей.


## Автор

Бедин Владислав ([MindlessMuse666](https://github.com/MindlessMuse666))
- GitHub: [MindlessMuse666](https://github.com/MindlessMuse666 "Владислав: https://github.com/MindlessMuse666")
- Telegram: [@mindless_muse](t.me/mindless_muse)
- Gmail: [mindlessmuse.666@gmail.com](mindlessmuse.666@gmail.com)
