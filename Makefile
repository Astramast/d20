install:
	@python3 -m venv .venv
	@. .venv/bin/activate
	@./.venv/bin/pip3 install -r requirements.txt

