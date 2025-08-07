# ”—🔗 ShortLink - Сервис сокращения ссылок

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.100.0-green.svg)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/vue.js-3.x-green.svg)](https://vuejs.org/)

**ShortLink** - современный микросервисный сервис для создания коротких ссылок с отслеживанием статистики и аналитикой.

## 🚀 Возможности

- ✂️ **Сокращение ссылок** - Превращайте длинные URL в короткие
- 📊 **Статистика** - Отслеживание кликов и географии переходов
- 🔐 **Аутентификация** - Защита приватных ссылок
- 📱 **API** - RESTful API для интеграции
- 🌐 **Web-интерфейс** - Удобная панель управления
- 🚀 **Высокая производительность** - Быстрые переходы по ссылкам

## 🏗️ Архитектура

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Auth Service  │    │   Link Service  │
│   (Vue.js)      │◄──►│   (FastAPI)     │◄──►│   (FastAPI)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                ▲                      ▲
                                │                      │
                        ┌─────────────────┐    ┌─────────────────┐
                        │   PostgreSQL    │    │   Redis         │
                        │   (Users)       │    │   (Cache)       │
                        └─────────────────┘    └─────────────────┘
```

## 📁 Структура проекта

```
shortlink/
├── apps/
│   ├── frontend/           # Веб-интерфейс (Vue.js)
│   └── services/           # Микросервисы
│       ├── auth/           # Сервис аутентификации
│       └── link/           # Сервис ссылок
├── infra/                  # Инфраструктура
│   ├── docker/             # Docker конфигурации
│   └── traefik/            # Reverse proxy
├── docs/                   # Документация
└── scripts/                # Скрипты автоматизации
```

## 🛠️ Быстрый старт

### Требования

- Docker и Docker Compose
- Python 3.11+
- Node.js 18+
- Poetry (для Python)
- Yarn (для Frontend)

### Установка

```bash
# Клонирование репозитория
git clone https://github.com/k1rson/shortlink.git
cd shortlink

# Установка зависимостей
make setup

# Запуск проекта
make dev
```

### Команды разработки

```bash
make dev        # Запустить проект
make stop       # Остановить проект
make logs       # Просмотр логов
make format     # Форматировать код
make test       # Запустить тесты
make clean      # Очистить проект
```

## 🌐 Доступ к сервисам

После запуска сервисы будут доступны по следующим адресам:

- **Web-интерфейс**: http://localhost:3000
- **Auth API**: http://api.localhost:8000
- **Link API**: http://api.localhost:8001
- **Traefik Dashboard**: http://localhost:8080

## 📚 API Документация

- **Auth Service**: http://api.localhost:8000/docs
- **Link Service**: http://api.localhost:8001/docs

## 🧪 Тестирование

```bash
# Запуск всех тестов
make test

# Запуск тестов для конкретного сервиса
cd apps/services/auth && poetry run pytest

# Запуск frontend тестов
cd apps/frontend/web && yarn test
```

## 📖 Документация

Подробная документация находится в директории [`docs/`](docs/):

- [Архитектура](docs/architecture.md)
- [API спецификация](docs/api/)
- [Руководство разработчика](docs/development.md)
- [Деплой в production](docs/deployment.md)

## 🤝 Вклад в проект

Мы приветствуем contributions! Чтобы внести свой вклад:

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для подробностей.

## 👥 Авторы

- **k1rson** - _Initial work_ - [@k1rson](https://github.com/k1rson)

Смотрите также список [contributors](https://github.com/k1rson/shortlink/contributors), которые участвовали в разработке проекта.

## 🙏 Благодарности

- [FastAPI](https://fastapi.tiangolo.com/) - для создания API
- [Vue.js](https://vuejs.org/) - для фронтенда
- [Docker](https://www.docker.com/) - для контейнеризации
- [Traefik](https://traefik.io/) - для reverse proxy

---

⭐ Если вам нравится проект, поставьте звезду! ⭐

[Вернуться к началу](#shortlink---сервис-сокращения-ссылок)
