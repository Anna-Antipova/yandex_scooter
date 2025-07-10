
Автотест проверяет сценарий создания заказа и получения информации по трек-номеру заказа через API.

## Шаги воспроизведения
1. Перейти в папку проекта:
```
cd /Users/annaantipova/Desktop/yandex_scooter
```

2. Создать и активировать виртуальное окружение:
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Установить зависимости:
```
pip install -r requirements.txt
```

4. Запустить тесты:
```
PYTHONPATH=. pytest test_order_flow.py

## Стек

- Python 3.x
- requests
- pytest
