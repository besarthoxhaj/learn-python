install:
	virtualenv env
	@brew update
	# brew install gfortran
	# Error: No available formula with the name "gfortran"
	# 	GNU Fortran is now provided as part of GCC, and can be installed with: brew install gcc
	@brew install gcc
	@brew install freetype
	@brew install zmq
	@brew install pyqt
	@env/bin/pip install -r requirements.txt
	@echo "You user! Execute: 'source env/bin/activate' to run the correct python and pip"

save:
	pip freeze > requirements.txt

watch:
	repyt server.py

.PHONY: install save
