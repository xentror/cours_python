all: plus_ou_moins soundbox

plus_ou_moins:
	pandoc --pdf-engine=xelatex -H head.tex -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm" --highlight-style pygments.theme plus-ou-moins.md -o plus_ou_moins.pdf

soundbox:
	cd SoundBox; make all;
