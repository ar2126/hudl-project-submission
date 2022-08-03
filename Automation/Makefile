help:
	@echo ""
	@echo "make setup-env		> sets up the virtual environment and installs required poetry packages"
	@echo "make clean-env		> cleans up the virtual environment and uninstalls poetry packages"

clean-env:
	rm -rf `poetry env info -p`
	poetry cache clear pypi.org --all -n

setup-env:
	poetry config experimental.new-installer false
	poetry install -vvv
	python3 util/update_configs.py