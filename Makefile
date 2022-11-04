install:
	cp spmd ${HOME}/.local/bin/
	cp spmd.1 ${HOME}/.local/share/man/man1/

man:
	pandoc --standalone --to man spmd.1.md -o spmd.1