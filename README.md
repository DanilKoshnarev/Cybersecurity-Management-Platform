
# Cybersecurity Management Platform

## Описание
Cybersecurity Management Platform - это комплексная система для управления кибербезопасностью, включающая модули для обнаружения и предотвращения угроз, управления инцидентами, анализа безопасности и обучения сотрудников.

## Структура проекта
Проект разделен на несколько слоев для улучшения читаемости и поддерживаемости кода:

- **Domain**: Основная бизнес-логика и правила.
- **Application**: Интерфейсы, юзкейсы и реализации для работы с данными.
- **Infrastructure**: Реализация деталей инфраструктуры, таких как модели данных, контроллеры и утилиты.
- **Presentation**: Визуализация данных и взаимодействие с пользователем.

## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone <URL репозитария>
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd cybersecurity_management
    ```
3. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск
Для запуска проекта выполните команду:
```bash
python src/Application.py
```

## Структура каталогов
```plaintext
cybersecurity_management/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── Threat.py
│   │   │   └── Incident.py
│   │   ├── repositories/
│   │   │   └── ThreatRepository.py
│   │   ├── services/
│   │   │   └── ThreatService.py
│   │   └── usecases/
│   │       └── ManageThreat.py
│   ├── infrastructure/
│   │   ├── models/
│   │   │   └── ThreatModel.py
│   │   ├── controllers/
│   │   │   └── ThreatController.py
│   ├── Application.py
├── tests/
│   └── ApplicationTests.py
├── requirements.txt
└── README.md
```

## Описание компонентов
### Domain
- **Threat.py**: Класс сущности угрозы.
- **Incident.py**: Класс сущности инцидента.
- **ThreatRepository.py**: Интерфейс репозитория угроз.

### Application
- **ManageThreat.py**: Юзкейс для управления угрозами.
- **ThreatService.py**: Сервис для управления угрозами.

### Infrastructure
- **ThreatModel.py**: Модель данных угрозы.
- **ThreatController.py**: Контроллер для управления угрозами.

### Presentation
- **DataView.py**: Представление для отображения угроз (если необходимо).

## Лицензия
Этот проект лицензирован под лицензией MIT. Для получения дополнительной информации см. файл LICENSE.
