# **Homework_2 - ...**

## **Описание**:

...

## **Установка**:

1. Клонируйте репозиторий

```
git@github.com:Alexandra-Chigrina/homework_2.git
```

2. В терминале инициализируйте Poetry и активируйте виртуальное окружение

```
poetry init
poetry shell
```

3. Установите зависимости

```
pip install -r requirements.txt
```

## **Использование**:

1. Запуск основного модуля.

   Запустите скрипты из модуля main.py в корне репозитория. 
   Модуль main.py связывает все функциональности проекта, вызывая ключевые функции.

```commandline
python main.py
```

2. Описание основных функций и классов

* В модуле src/base_product.py создан базовый абстрактный класс BaseProduct.
* В модуле src/base_features.py создан базовый абстрактный класс BaseFeatures.
* В модуле src/print_mixin.py создан класс-миксин PrintMixin, печатающий при создании объекта в консоль информацию 
  о том, от какого класса и с какими параметрами был создан объект.
* В модуле src/product.py создан класс Product (наследник класса BaseProduct, PrintMixin), 
  который представляет товар с его характеристиками.
* В модуле src/category.py создан класс Category (наследник класса BaseFeatures), представляет категорию товаров, 
  содержащую список продуктов.
* В модуле src/smartphone.py создан класс "Смартфон" (Smartphone) (наследник класса Product).
* В модуле src/lawngrass.py создан класс "Трава газонная" (LawnGrass) (наследник класса Product).
* В модуле src/order.py создан класс Order (наследник класса BaseFeatures), в котором дается информация о том, 
  какой товар был куплен, количество купленного товара, а также итоговая стоимость.



## **Примеры работы**:

...


## **Тестирование**

1. Установите pytest через Poetry

```
poetry add --group dev pytest
```

2. Запустить тестирование можно из модулей 'test_name', находящихся в папке 'tests' или в терминале

```
pytest
```

3. Для анализа покрытия кода тестами установите библиотеку 'pytest-cov'

```commandline
poetry add --group dev pytest-cov
```

4. Запустите тесты с оценкой покрытия

```commandline
pytest --cov=src --cov-report=term-missing tests/
```


## **Структура проекта**

├── src/                          # Основной код
│   ├── base_features.py          # Создание абстрактного класса BaseFeatures
│   ├── base_product.py           # Создание абстрактного класса BaseProduct
│   ├── category.py               # Создание класса Category
│   ├── lawngrass.py              # Создание класса LawnGrass
│   ├── order.py                  # Создание класса Order
│   ├── print_mixin.py            # Создание класса-миксина PrintMixin
│   ├── product.py                # Создание класса Product
│   ├── product_iterator.py       # Создание класса ProductIterator
│   ├── smartphone.py             # Создание класса Smartphone
│   ├── utils.py                  # Утилиты (чтение файлов, создание объектов класса и т. д.)
├── data/                         # Данные
│   ├── products.json             # Данные о категориях и продуктах
├── tests/                        # Тесты
│   ├── conftest.py               # Фикстуры для тестов
│   ├── test_category.py          # Тесты для category.py
│   ├── test_lawngrass.py         # Тесты для lawngrass.py
│   ├── test_order.py             # Тесты для order.py
│   ├── test_product.py           # Тесты для product.py
│   ├── test_product_iterator.py  # Тесты для product_iterator.py
│   ├── test_smartphone.py        # Тесты для smartphone.py
│   ├── test_utils.py             # Тесты для utils.py
├── main.py                       # Основная логика
├── .venv                         # Виртуальное окружение
├── .gitignore                    # Исключения файлов из Git
├── .config.py                    # Файл конфигурации
├── .flake8                       # Настройки линтера Flake8
├── .coverage                     # Отчеты покрытия кода тестами
├── .poetry.lock                  # Фиксированные зависимости проекта
├── .pyproject.toml               # Основной конфигурационный файл проекта
├── README.md                     # Документация
