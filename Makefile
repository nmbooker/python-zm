
ROPKGBASE=pkg/PyZM

all: riscospkg

# .pyc,ffd is what you end up with if the file comes from RISC OS
clean:
	$(RM) zm/*.pyc zm/*.pyc,ffd
	$(RM) -r '$(ROPKGBASE)'

zip:
	git archive -o python-zm.zip HEAD

riscospkg:
	mkdir -p '$(ROPKGBASE)/!PyZM/Lib'
	mkdir -p '$(ROPKGBASE)/!PyZM/Lib/zm'
	cp zm/*.py '$(ROPKGBASE)/!PyZM/Lib/zm/'
	mkdir -p '$(ROPKGBASE)/!PyZM/Lib/zmui'
	cp zmui/*.py '$(ROPKGBASE)/!PyZM/Lib/zmui/'
	cp 'riscos/!Run,feb' 'riscos/!Boot,feb' 'riscos/AddToPath,ffc' '$(ROPKGBASE)/!PyZM/'
