# Syllabus.uno — лабораторні роботи з Теорії програмних систем

![Python CI Application](https://github.com/mazurenko-stud/syllabus/actions/workflows/python-app.yml/badge.svg?branch=main)

Репозиторій створено для виконання лабораторних робіт з дисципліни «Теорія програмних систем».

## Тема індивідуального завдання

Вебсистема **Syllabus.uno** для стандартизованого формування, зберігання та публікації робочих програм і силабусів закладу вищої освіти.

## Функціональність репозиторію

- зберігання звітів до лабораторних робіт;
- зберігання UML-діаграм і PlantUML-коду;
- демонстрація роботи Git, GitHub Pull Requests і reviewers;
- налаштування CI-пайплайну GitHub Actions;
- автоматична перевірка Python-коду за допомогою flake8;
- запуск unit-тестів для демонстраційного модуля calculator.py;
- демонстрація використання GitHub Secrets;
- робота з GitHub Issues та GitHub Projects.

## Запуск тестів локально

```bash
python -m unittest test_calculator.py
```

## Перевірка стилю коду локально

```bash
pip install flake8
flake8 calculator.py test_calculator.py
```

## Структура основних файлів

```text
.github/workflows/python-app.yml
calculator.py
test_calculator.py
docs/
reports/
README.md
```
