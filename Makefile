install:
	pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt
test:
	pytest tests/
format-check:
	black --check ./src ./tests
	flake8 ./src ./tests
format:
	black ./src ./tests
	isort ./src ./tests
