.PHONY: build
build:
	python3 -m pip install --upgrade build
	python3 -m build


.PHONY: env
env:
	python3 -m pip install --upgrade virtualenv
	python3 -m virtualenv --clear -p python3 .pyflicka.env


.PHONY: install
install:
	. .pyflicka.env/bin/activate && \
	python3 -m pip install .


.PHONY: install-pkg
install-pkg:
	. .pyflicka.env/bin/activate && \
	python3 -m pip install pyflicka.tar.gz


.PHONY: clean
clean:
	rm -rf .pyflicka.env
	find -iname '*.pyc' -delete


.PHONY: start
start:
	. .pyflicka.env/bin/activate && \
	python3 -m pyflicka >> pyflicka_output.log 2>&1 &


.PHONY: stop
stop:
	kill -9 $$(ps -aux | grep -P 'pyflicka[/\s]' | grep -Po '\+ (\d)+ ' | grep -Po '\d+') && \
	echo "\033[92m Stoped Pyflicka running\033[0m" || \
	echo "\033[91m There is no Pyflicka running\033[0m"

.PHONY: update
update: stop env install-pkg start


.PHONY: dev-install
dev-install: env
	. .pyflicka.env/bin/activate && \
	python3 setup.py develop


.PHONY: dev
dev: dev-install
	. .pyflicka.env/bin/activate && \
	python3 -m pyflicka
