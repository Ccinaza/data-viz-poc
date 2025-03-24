# Start all services
start:
	@docker-compose up -d

# Stop all services
stop:
	@docker-compose down

# Restart the services
restart:
	@make stop
	@make start

# Remove containers, networks, and volumes
clean:
	@docker-compose down -v

# Show running containers
status:
	@docker ps --filter "name=metabase"

# Tail Metabase logs
logs:
	@docker-compose logs -f metabase
