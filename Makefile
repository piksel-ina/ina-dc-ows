COMPOSE_FILE := compose.yml
PROJECT_NAME := inadc-ows
PIKSEL_NETWORK ?= piksel-net

DOCKER_COMPOSE = docker compose -f $(COMPOSE_FILE) -p $(PROJECT_NAME)

BLUE=\033[34;1m
GREEN=\033[32m
YELLOW=\033[33m
NC=\033[0m

.PHONY: help
help: ## Show this help
	@echo ""
	@echo "$(BLUE)Make Commands$(NC)"
	@echo ""
	@awk 'BEGIN {FS = ":.*##";} \
	     /^[a-zA-Z0-9_.-]+:.*##/ { printf "  $(GREEN)%-22s$(NC) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: build up down stop restart ps logs bash-ows
build: ## Build the OWS Docker image
	@echo "$(BLUE)Building OWS image...$(NC)"
	$(DOCKER_COMPOSE) build

up: ## Start OWS service
	@echo "$(BLUE)Starting OWS service...$(NC)"
	$(DOCKER_COMPOSE) up -d

down: ## Stop and remove OWS containers
	@echo "$(BLUE)Stopping OWS service...$(NC)"
	$(DOCKER_COMPOSE) down

stop: ## Stop OWS containers (without removing)
	@echo "$(BLUE)Stopping OWS service...$(NC)"
	$(DOCKER_COMPOSE) stop

restart: ## Restart OWS service
	@echo "$(BLUE)Restarting OWS service...$(NC)"
	$(DOCKER_COMPOSE) restart

ps: ## Show service status
	@echo "$(BLUE)OWS service status:$(NC)"
	$(DOCKER_COMPOSE) ps

logs: ## Tail logs (Ctrl+C to exit)
	@echo "$(BLUE)Viewing OWS logs...$(NC)"
	$(DOCKER_COMPOSE) logs -f

bash-ows: ## Open a shell in the OWS container
	@echo "$(BLUE)Opening shell in OWS container...$(NC)"
	$(DOCKER_COMPOSE) exec ows bash

.PHONY: init-schema init-layers init
init-schema: ## Create OWS database schema (run once after DB init)
	@echo "$(BLUE)Creating OWS schema...$(NC)"
	$(DOCKER_COMPOSE) exec ows datacube-ows-update --schema --write-role

init-layers: ## Update materialised views for all layers
	@echo "$(BLUE)Updating OWS layers...$(NC)"
	$(DOCKER_COMPOSE) exec ows datacube-ows-update s2_l2a s2_geomad_annual_spectral s2_geomad_annual_120 s2_geomad_annual_indices s2_geomad_annual_statistics

init: init-schema init-layers ## Full init: schema + layer updates

.PHONY: test test-unit compile-deps
test: ## Run all tests
	@echo "$(BLUE)Running tests...$(NC)"
	PYTHONPATH=$(CURDIR) .venv/bin/pytest -v tests/

test-unit: ## Run unit tests only
	@echo "$(BLUE)Running unit tests...$(NC)"
	PYTHONPATH=$(CURDIR) .venv/bin/pytest -v tests/

compile-deps: ## Compile dependency lockfile
	@echo "$(BLUE)Compiling dependencies...$(NC)"
	uv lock --python 3.12
	@echo "$(GREEN)Dependencies compiled!$(NC)"
