agent=keyboard_agent

run:
	$(PWD)/miniconda_pygame/bin/python ./game.py --agent $(agent)

download_miniconda:
	if [[ `uname` == 'Darwin' ]]; then make download_miniconda_macos; else make download_miniconda_linux; fi

install: download_miniconda
	chmod 755 ./miniconda.sh
	./miniconda.sh -b -p $(PWD)/miniconda_pygame -f && conda config --set auto_activate_base false
	$(PWD)/miniconda_pygame/bin/pip install pygame numpy pyyaml
	rm -rf ./miniconda.sh
    
download_miniconda_linux:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O miniconda.sh
	
clean:
	rm -rf ./miniconda_pygame

download_miniconda_macos:
	if [[ `uname -m` == 'x86_64' ]]; then make download_miniconda_macos_x86_64; else make download_miniconda_macos_m1; fi

download_miniconda_macos_x86_64:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-x86_64.sh -O miniconda.sh

download_miniconda_macos_m1:
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-arm64.sh -O miniconda.sh

