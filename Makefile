install:
	pip install --upgrade pip &&\
		pip install -r requiremnets.txt

test:
	python -m pytest -vvv test_main.py

format:
	black *.py

run:
	python main.py

deploy:
	uvicorn main:app --reload

kill:
	sudo killall uvicorn

lint:
	pylint --disable=R,C main.py