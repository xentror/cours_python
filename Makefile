all: plus_ou_moins soundbox

plus_ou_moins:
	cd PlusOuMoins; make all;

soundbox:
	cd SoundBox; make all;

clean:
	cd SoundBox; make clean;
	cd PlusOuMoins; make clean;
