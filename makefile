build:
	black gcmanager/ tests/ --check --verbose --diff --color
	isort gcmanager/ tests/ --check --diff
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
	ruff check --select="COM812,COM819,F401,I001,I002,W291,W292,W293,UP,SIM" gcmanager/ tests/ --fix
	black gcmanager/ tests/
	isort gcmanager/ tests/
