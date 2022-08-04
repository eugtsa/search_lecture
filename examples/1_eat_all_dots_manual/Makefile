agent=keyboard_agent

run:
	$(PWD)/miniconda_pygame/bin/python ./game.py --agent $(agent)

run_no_gui:
	$(PWD)/miniconda_pygame/bin/python ./game.py --agent $(agent) --daemon

install: download_miniconda
	chmod 755 ./miniconda.sh
	./miniconda.sh -b -p $(PWD)/miniconda_pygame -f && $(PWD)/miniconda_pygame/bin/conda config --set auto_activate_base false
	PYTHONPATH=$(PWD)/miniconda_pygame/bin/python;$(PWD)/miniconda_pygame/bin/python -m pip install pygame numpy pyyaml
	rm -rf ./miniconda.sh

download_miniconda:
	bash -c "if [[ `uname` == 'Darwin' ]]; then make download_miniconda_macos; else make download_miniconda_linux; fi"
    
download_miniconda_linux:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O miniconda.sh
	
clean:
	rm -rf ./miniconda_pygame
	rm -rf ./miniconda.sh

download_miniconda_macos:
	bash -c "if [[ `uname -m` == 'x86_64' ]]; then make download_miniconda_macos_x86_64; else make download_miniconda_macos_m1; fi"

download_miniconda_macos_x86_64:
	curl https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-x86_64.sh -o miniconda.sh

download_miniconda_macos_m1:
	curl https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-arm64.sh -o miniconda.sh

