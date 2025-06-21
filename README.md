# Selenium Automation Testing Project

Проект автоматизированного тестирования веб-приложения с использованием Python, Selenium WebDriver и pytest.

## 📋 Описание

Данный проект содержит автотесты для интернет-магазина [selenium1py.pythonanywhere.com](http://selenium1py.pythonanywhere.com/), реализованные по паттерну Page Object Model (POM). Тесты покрывают основной функционал: регистрацию пользователей, добавление товаров в корзину, проверку корзины и навигацию по сайту.

## 🛠 Технологии

- **Python 3.x** - основной язык программирования
- **Selenium WebDriver 4.33.0** - автоматизация браузера
- **pytest 8.3.5** - фреймворк для тестирования
- **Chrome/Firefox WebDriver** - драйверы браузеров

## 📁 Структура проекта

```
project/
├── pages/                     # Page Object классы
│   ├── __init__.py
│   ├── base_page.py          # Базовый класс для всех страниц
│   ├── main_page.py          # Главная страница
│   ├── login_page.py         # Страница входа/регистрации
│   ├── product_page.py       # Страница товара
│   ├── basket_page.py        # Страница корзины
│   └── locators.py           # Локаторы элементов
├── test_main_page.py         # Тесты главной страницы
├── test_product_page.py      # Тесты страницы товара
├── conftest.py               # Конфигурация pytest и фикстуры
├── requirements.txt          # Зависимости проекта
├── .gitignore               # Игнорируемые файлы
└── README.md                # Документация проекта
```

## 🚀 Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/hppdenjoyer/stepik_final_task
cd stepik_final_task
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Установка драйверов браузеров
- **Chrome**: Скачайте [ChromeDriver](https://chromedriver.chromium.org/) и добавьте в PATH
- **Firefox**: Скачайте [GeckoDriver](https://github.com/mozilla/geckodriver/releases) и добавьте в PATH

## 🎯 Запуск тестов

### Базовый запуск
```bash
pytest
```

### Запуск с выбором браузера
```bash
# Chrome (по умолчанию)
pytest --browser_name=chrome

# Firefox
pytest --browser_name=firefox
```

### Запуск с выбором языка
```bash
pytest --language=ru
pytest --language=en
```

### Запуск конкретных тестов
```bash
# Все тесты главной страницы
pytest test_main_page.py

# Все тесты страницы товара
pytest test_product_page.py

# Тесты с определенным маркером
pytest -m login_guest
pytest -m user_product
```

### Запуск с подробными логами
```bash
pytest -v -s
```

## 📝 Page Object Model

Проект использует паттерн Page Object Model для лучшей организации кода:

### Специализированные страницы
- **BasePage** - базовый класс содрижт общие методы
- **MainPage** - главная страница магазина
- **LoginPage** - страница входа/регистрации с методом `register_new_user()`
- **ProductPage** - страница товара с методами добавления в корзину
- **BasketPage** - страница корзины с проверками содержимого

## ⚙️ Конфигурация

### Параметры запуска
В `conftest.py` настроены следующие параметры:
- `--browser_name` - выбор браузера (chrome/firefox)
- `--language` - выбор языка интерфейса

## 🔍 Маркеры pytest

- `@pytest.mark.login_guest` - тесты входа для гостей
- `@pytest.mark.user_product` - тесты для авторизованных пользователей
- `@pytest.mark.xfail` - тесты, которые ожидаемо падают









