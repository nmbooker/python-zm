
all: riscospkg

# .pyc,ffd is what you end up with if the file comes from RISC OS
clean:
	$(RM) zm/*.pyc zm/*.pyc,ffd
	$(RM) -r 'pkg/!PyZM'

zip:
	git archive -o python-zm.zip HEAD

riscospkg:
	mkdir -p 'pkg/!PyZM/Lib'
	mkdir -p 'pkg/!PyZM/Lib/zm'
	cp zm/*.py 'pkg/!PyZM/Lib/zm/'
	mkdir -p 'pkg/!PyZM/Lib/zmui'
	cp zmui/*.py 'pkg/!PyZM/Lib/zm/'
	cp 'riscos/!Run,feb' 'riscos/!Boot,feb' 'riscos/AddToPath,ffc' 'pkg/!PyZM/'
