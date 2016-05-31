all:
	python cleanRDB.py
	-rm *.pyc
	script -c "time python main.py" log
clean:
	-rm *.pyc
	python cleanRDB.py
