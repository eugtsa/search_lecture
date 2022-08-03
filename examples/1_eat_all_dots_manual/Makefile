agent=keyboard_agent

run:
	$(PWD)/miniconda_pygame/bin/python ./game.py --agent $(agent)

install:
	bash -c "if [[ $OSTYPE == 'darwin'* ]]; then make install_macos; else make install_linux; fi"

install_linux:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O miniconda.sh
	chmod 755 ./miniconda.sh
	./miniconda.sh -b -p $(PWD)/miniconda_pygame -f && conda config --set auto_activate_base false
	$(PWD)/miniconda_pygame/bin/pip install pygame numpy pyyaml
	rm -rf ./miniconda.sh

clean:
	rm -rf ./miniconda_pygame

install_macos:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-x86_64.sh -O miniconda.sh
	chmod 755 ./miniconda.sh
	./miniconda.sh -b -p $(PWD)/miniconda_pygame -f && conda config --set auto_activate_base false
	$(PWD)/miniconda_pygame/bin/pip install pygame numpy pyyaml
	rm -rf ./miniconda.sh