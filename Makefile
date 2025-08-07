PROJECT_NAME = url-service
COMPOSE_FILE = docker-compose.yml

.PHONY: build up down restart logs shell clean ps

build:
	docker compose -f infra/docker/$(COMPOSE_FILE) build

up:
	docker compose -f infra/docker/$(COMPOSE_FILE) up -d

down:
	docker compose -f infra/docker/$(COMPOSE_FILE) down

restart: down up

logs:
	docker compose -f infra/docker/$(COMPOSE_FILE) logs -f

logs-%:
	docker compose -f infra/docker/$(COMPOSE_FILE) logs -f $*

shell:
	docker compose -f infra/docker/$(COMPOSE_FILE) exec app /bin/bash

shell-%:
	docker compose -f infra/docker/$(COMPOSE_FILE) exec $* /bin/bash

ps:
	docker compose -f infra/docker/$(COMPOSE_FILE) ps

clean:
	docker compose -f infra/docker/$(COMPOSE_FILE) down -v --remove-orphans

run: build up
