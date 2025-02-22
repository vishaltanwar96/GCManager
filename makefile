build:
	ruff format --check --diff gcmanager/ tests/
	mypy
	ruff check gcmanager/ tests/
	bandit -r gcmanager --verbose
	nerdctl compose -f mongo-for-testing.yml up -d
	coverage erase
	coverage run -mp unittest discover tests/unit --verbose
	coverage run -mp unittest discover tests/integration --verbose
	nerdctl compose -f mongo-for-testing.yml down
	coverage combine
	coverage report
style:
	ruff check --select="COM818,F401,I001,I002,W291,W292,W293,UP,SIM" gcmanager/ tests/ --fix
	ruff format gcmanager/ tests/
