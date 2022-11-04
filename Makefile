install:
	cp spmd ${HOME}/.local/bin/
	cp spmd.1 ${HOME}/.local/share/man/man1/

html:
	mandoc -T html -O style=/mandoc.css spmd.1 > spmd.1.html